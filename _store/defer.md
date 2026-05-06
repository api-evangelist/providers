---
aid: defer
name: Defer
description: Defer was a TypeScript-first background job and workflow automation platform for Node.js applications that let developers schedule, queue, and orchestrate serverless functions with built-in retries, throttling, concurrency controls, and scheduled (CRON) execution. Defer integrated with frameworks such as Next.js, Remix, and SvelteKit through an SDK and a managed control plane. The defer.run service has since transitioned and the defer.run domain currently redirects to digger.tools; this entry preserves the historical profile and links to the surviving documentation, GitHub organization, and references.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/defer/refs/heads/main/apis.yml
specificationVersion: '0.19'
xType: company
access: 3rd-Party
position: Consuming
tags:
  - Background Jobs
  - CRON
  - Developer-First
  - Node.js
  - Queues
  - Scheduling
  - Serverless
  - TypeScript
  - Workflow Automation
created: '2026-03-27'
modified: '2026-04-28'
apis:
  - aid: defer:defer-platform
    name: Defer Platform
    description: The Defer platform exposes a TypeScript SDK for declaring deferred functions and a managed control plane that schedules, queues, retries, and observes their execution. Functions are defined with decorators such as defer() and defer.cron() and invoked from application code; the platform handled queuing, scaling, and observability transparently.
    humanURL: https://www.defer.run
    tags:
      - Background Jobs
      - SDK
      - Workflow Automation
    properties:
      - type: Documentation
        url: https://docs.defer.run
      - type: GitHub Organization
        url: https://github.com/defer-run
common:
  - type: Website
    url: https://www.defer.run
  - type: Documentation
    url: https://docs.defer.run
  - type: GitHub
    url: https://github.com/defer-run
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
