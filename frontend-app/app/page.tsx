"use client"; // add this directive at the top to enable client-side interactivity


import { useState } from "react";
import Image from "next/image";
import { RSCPathnameNormalizer } from "next/dist/server/normalizers/request/rsc";


export default function Home() {

  const [wikiUrl, setWikiUrl] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const flaskBackend = "http://localhost:5000";

  const handleInputChange = (e) => {
    setWikiUrl(e.target.value);
  };

  const handleInputChangeQuestion = (e) => {
    setQuestion(e.target.value);
  };

  async function handleSubmit() {
    // You can do something with the wikiUrl here, e.g. validation or fetch content
    alert(`Entered Wikipedia URL: ${wikiUrl}`);
    const response = await fetch(flaskBackend + '/set_wikipedia_url', {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ wikipedia_url: wikiUrl })
    });
    return response;
  };

  async function handleSubmitQuestion() {
    const response = await fetch(flaskBackend + '/query', {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ query: question })
    });
    const resp = await response.json();
    setAnswer(resp.answer);
    alert(`Response: ${answer}`);
    return resp.answer;
  };

  return (
    <div className="font-sans grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <input
          type="url"
          placeholder="Enter Wikipedia URL"
          value={wikiUrl}
          onChange={handleInputChange}
          className="border border-gray-300 rounded px-2 py-1"
        />
        <button
          onClick={handleSubmit}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Submit
        </button>
        <input
          type="text"
          placeholder="Enter question here"
          value={question}
          onChange={handleInputChangeQuestion}
          className="border border-gray-300 rounded px-2 py-1"
        />
        <button
          onClick={handleSubmitQuestion}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Submit
        </button>
        <div>{answer}</div>
      </main>
    </div>
  );
}
