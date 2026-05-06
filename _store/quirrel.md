---
aid: quirrel
name: Quirrel
description: Quirrel is an open source job queueing and workflow scheduling service designed for serverless and containerized JavaScript and TypeScript applications. It enables developers to enqueue, schedule, retry, and orchestrate background jobs in environments such as Next.js, Blitz.js, Redwood, Remix, SvelteKit, Nuxt.js, Express, Vercel, and Netlify Functions. Quirrel was acquired by Netlify in 2022 and remains available as an open source project.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Tools
  - Job Queues
  - Workflow Automation
  - Background Jobs
  - Serverless
  - Scheduling
url: https://raw.githubusercontent.com/api-evangelist/quirrel/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: quirrel:quirrel
    name: Quirrel
    description: Quirrel provides a JavaScript and TypeScript SDK for enqueuing, scheduling, retrying, and managing background jobs in serverless and containerized applications. The Queue API exposes methods such as enqueue, enqueueMany, get, getById, invoke, and delete to manage job lifecycle and supports recurring jobs via cron expressions, delayed execution, exclusive jobs, and configurable retry policies. Quirrel is framework agnostic and integrates with Next.js, Redwood, Remix, SvelteKit, Nuxt.js, Blitz.js, Vercel, Netlify, and Express.
    humanURL: https://quirrel.dev
    tags:
      - Job Queues
      - Workflow Automation
      - Background Jobs
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.quirrel.dev
      - type: GettingStarted
        url: https://docs.quirrel.dev/getting-started
      - type: SourceCode
        url: https://github.com/quirrel-dev/quirrel
      - type: SDKs
        url: https://www.npmjs.com/package/quirrel
common:
  - type: Website
    url: https://quirrel.dev
  - type: Documentation
    url: https://docs.quirrel.dev
  - type: SourceCode
    url: https://github.com/quirrel-dev/quirrel
  - type: Acquisition
    url: https://www.netlify.com/blog/quirrel-is-joining-netlify/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
