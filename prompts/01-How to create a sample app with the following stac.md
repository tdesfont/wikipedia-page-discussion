<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# How to create a sample app with the following stack:

Next.js 15 with App Router
TypeScript
Tailwind CSS

Here is a step-by-step guide to create a sample app using Next.js 15 with App Router, TypeScript, and Tailwind CSS:

### Step 1: Create a new Next.js 15 app with TypeScript and App Router

Run this command in your terminal:

```
npx create-next-app@latest my-app
```

During the prompts:

- Choose to use TypeScript
- Choose App Router support
- Enable ESLint if desired

This will generate a new Next.js 15 project with TypeScript and the App Router enabled.[^2][^8][^9]

### Step 2: Install Tailwind CSS and its dependencies

Move into your project directory and install Tailwind CSS and its PostCSS plugin:

```
cd my-app
npm install -D tailwindcss postcss @tailwindcss/postcss
```

Generate the Tailwind config files:

```
npx tailwindcss init -p
```


### Step 3: Configure Tailwind CSS for Next.js 15

In your `tailwind.config.js` file, set the content paths to include your app directory:

```js
export default {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```


### Step 4: Add Tailwind directives to global CSS

Create a CSS file `app/globals.css` (or similar) and add Tailwind base, components, and utilities:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```


### Step 5: Import global CSS in root layout

In `app/layout.tsx`, import the global CSS file:

```ts
import './globals.css';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```


### Step 6: Start the development server

Run the dev server:

```
npm run dev
```

You can now use Tailwind utility classes directly in your components inside the `app` directory with TypeScript support.

### Bonus: Example page component with Tailwind and TypeScript

In your `app/page.tsx` add a simple welcome page:

```ts
export default function Page() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js 15 with Tailwind CSS and TypeScript!</h1>
    </main>
  );
}
```

This setup covers the modern Next.js 15 app router-based project with TypeScript and Tailwind CSS styling, following the latest best practices and tooling.[^1][^3][^5][^9][^2]

If you want a starter boilerplate with the entire setup including eslint, vitest, testing, and more, there are open-source starter projects available that you can clone and customize.[^6]

Let me know if you want instructions for anything more specific or advanced!
<span style="display:none">[^10][^4][^7]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.youtube.com/watch?v=Jol0vCitur4

[^2]: https://softwaremill.com/modern-full-stack-application-architecture-using-next-js-15/

[^3]: https://nextjs.org/docs/app/getting-started/css

[^4]: https://www.youtube.com/watch?v=ugxI1o5SyMs

[^5]: https://dev.to/rhythmsaha/how-to-set-up-a-nextjs-project-with-typescript-and-tailwind-css-2hk7

[^6]: https://github.com/ixartz/Next-js-Boilerplate

[^7]: https://tailwindcss.com/docs/guides/nextjs

[^8]: https://nextjs.org/docs/app/getting-started/installation

[^9]: https://nextjs.org/docs/app/getting-started

[^10]: https://kombai.com/tailwind/tailwind-css-nextjs-setup-and-example/

