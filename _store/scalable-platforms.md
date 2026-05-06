---
name: Scalable Platforms
description: A subject-matter collection covering APIs, tools, and platforms for building and deploying scalable platform infrastructure. This topic encompasses Platform-as-a-Service (PaaS) providers, developer experience platforms, deployment automation, serverless computing, container platforms, and the tools that abstract infrastructure management so teams can focus on application delivery. Covers Railway, Render, Fly.io, Heroku, Vercel, Netlify, and Cloudflare Workers.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/scalable-platforms/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Cloud Infrastructure
  - Deployment
  - Developer Experience
  - DevOps
  - PaaS
  - Platform
  - Scalability
  - Serverless
apis:
  - name: Vercel REST API
    description: Vercel is the frontend cloud platform for deploying Next.js, React, and other JavaScript frameworks with zero configuration. The Vercel REST API manages deployments, projects, domains, environment variables, edge functions, and team access. Provides global edge network with automatic scaling.
    image: https://vercel.com/favicon.ico
    humanUrl: https://vercel.com/
    baseUrl: https://api.vercel.com
    tags:
      - CDN
      - Deployment
      - Edge Computing
      - Frontend
      - Next.js
      - Serverless
      - Vercel
    properties:
      - type: Documentation
        url: https://vercel.com/docs/rest-api
      - type: OpenAPI
        url: https://openapi.vercel.sh/
      - type: Getting Started
        url: https://vercel.com/docs
      - type: Pricing
        url: https://vercel.com/pricing
      - type: SDK
        url: https://github.com/vercel/sdk
    contact:
      - type: Community
        url: https://github.com/orgs/vercel/discussions
      - type: GitHub
        url: https://github.com/vercel/vercel
  - name: Netlify API
    description: Netlify is a web platform for building, deploying, and serving modern web projects. The Netlify API manages sites, deploys, environment variables, build hooks, functions, forms, identity, and DNS records. Features atomic deploys and instant rollbacks.
    image: https://www.netlify.com/favicon/favicon-32x32.png
    humanUrl: https://www.netlify.com/
    baseUrl: https://api.netlify.com/api/v1
    tags:
      - CDN
      - CI/CD
      - Deployment
      - Frontend
      - JAMstack
      - Netlify
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.netlify.com/api/get-started/
      - type: OpenAPI
        url: https://open-api.netlify.com/
      - type: Getting Started
        url: https://docs.netlify.com/
      - type: Pricing
        url: https://www.netlify.com/pricing/
      - type: SDK
        url: https://github.com/netlify/js-client
    contact:
      - type: Community
        url: https://community.netlify.com/
      - type: GitHub
        url: https://github.com/netlify/netlify-api
  - name: Cloudflare API
    description: Cloudflare's platform API manages DNS, CDN, Firewall rules, Workers (serverless edge functions), Pages (JAMstack deployments), R2 (object storage), D1 (serverless SQLite), KV, and Durable Objects. Powers globally distributed scalable applications at the edge.
    image: https://www.cloudflare.com/favicon.ico
    humanUrl: https://www.cloudflare.com/
    baseUrl: https://api.cloudflare.com/client/v4
    tags:
      - CDN
      - Cloudflare
      - DNS
      - Edge Computing
      - Security
      - Serverless
      - Workers
    properties:
      - type: Documentation
        url: https://developers.cloudflare.com/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/cloudflare/api-schemas/main/openapi.yaml
      - type: Getting Started
        url: https://developers.cloudflare.com/
      - type: Pricing
        url: https://www.cloudflare.com/plans/
      - type: SDK
        url: https://github.com/cloudflare/cloudflare-typescript
    contact:
      - type: Community
        url: https://community.cloudflare.com/
      - type: GitHub
        url: https://github.com/cloudflare
  - name: Heroku Platform API
    description: Heroku pioneered the "git push" deployment model and remains a leading PaaS for rapid application deployment. The Heroku Platform API manages apps, dynos, config vars, add-ons, pipelines, review apps, spaces (private networking), and team access. Owned by Salesforce.
    image: https://www.herokucdn.com/favicons/favicon.ico
    humanUrl: https://www.heroku.com/
    baseUrl: https://api.heroku.com
    tags:
      - Deployment
      - Dynos
      - Heroku
      - PaaS
      - Pipelines
      - Salesforce
    properties:
      - type: Documentation
        url: https://devcenter.heroku.com/articles/platform-api-reference
      - type: OpenAPI
        url: https://devcenter.heroku.com/api-docs
      - type: Getting Started
        url: https://devcenter.heroku.com/start
      - type: Pricing
        url: https://www.heroku.com/pricing
    contact:
      - type: Support
        url: https://help.heroku.com/
      - type: Community
        url: https://help.heroku.com/
  - name: Fly.io Machines API
    description: Fly.io deploys Docker containers globally on its own hardware, with low-latency routing to the nearest region. The Machines API manages apps, machines (VMs), volumes, networks, secrets, and certificates. In 2026, Fly.io supports managed Postgres, GPU instances, Kubernetes, object storage, and scale-to-zero.
    image: https://fly.io/static/images/brand/logo-landscape-dark.svg
    humanUrl: https://fly.io/
    baseUrl: https://api.machines.dev/v1
    tags:
      - Containers
      - Deployment
      - Edge Computing
      - Fly.io
      - Global Deployment
      - Scale To Zero
    properties:
      - type: Documentation
        url: https://fly.io/docs/machines/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/superfly/fly-openapi/refs/heads/main/openapi.yaml
      - type: Getting Started
        url: https://fly.io/docs/getting-started/
      - type: Pricing
        url: https://fly.io/docs/about/pricing/
      - type: SDK
        url: https://github.com/superfly/fly-go
    contact:
      - type: Community
        url: https://community.fly.io/
      - type: GitHub
        url: https://github.com/superfly
  - name: Railway API
    description: Railway is a modern deployment platform with usage-based pricing and arguably the best developer experience of any deployment platform. Launched in 2020, by 2026 it has matured with support for persistent volumes, private networking, cron jobs, TCP proxy, and one-click database deployments. The API manages projects, services, deployments, environments, and variables.
    image: https://railway.app/favicon.ico
    humanUrl: https://railway.app/
    baseUrl: https://backboard.railway.app/graphql/v2
    tags:
      - Containers
      - Deployment
      - Developer Experience
      - PaaS
      - Railway
      - Usage-Based Pricing
    properties:
      - type: Documentation
        url: https://docs.railway.app/reference/public-api
      - type: Getting Started
        url: https://docs.railway.app/
      - type: Pricing
        url: https://railway.app/pricing
      - type: SDK
        url: https://github.com/railwayapp/cli
    contact:
      - type: Community
        url: https://discord.com/invite/railway
      - type: GitHub
        url: https://github.com/railwayapp
  - name: Render API
    description: Render positioned itself as the modern Heroku with a free tier, managed databases, background workers, cron jobs, and static sites. The Render API manages services, deploys, environment groups, and custom domains. By 2026, Render supports auto-scaling, private networking, and managed Redis.
    image: https://render.com/favicon.ico
    humanUrl: https://render.com/
    baseUrl: https://api.render.com/v1
    tags:
      - Containers
      - Deployment
      - Managed Databases
      - PaaS
      - Render
      - Serverless
    properties:
      - type: Documentation
        url: https://api-docs.render.com/reference/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/renderinc/openapi-specs/main/openapi.yaml
      - type: Getting Started
        url: https://render.com/docs/
      - type: Pricing
        url: https://render.com/pricing
    contact:
      - type: Community
        url: https://community.render.com/
      - type: GitHub
        url: https://github.com/render-oss
  - name: Northflank API
    description: Northflank is a DevOps platform providing container deployment, managed databases, job scheduling, preview environments, and full Kubernetes-based infrastructure. The Northflank API manages projects, services, databases, secrets, and pipelines. Supports BYOC (Bring Your Own Cloud) for running on AWS, GCP, or Azure.
    image: https://northflank.com/favicon.ico
    humanUrl: https://northflank.com/
    baseUrl: https://api.northflank.com/v1
    tags:
      - BYOC
      - CI/CD
      - Containers
      - Deployment
      - Kubernetes
      - Managed Databases
      - Northflank
      - PaaS
    properties:
      - type: Documentation
        url: https://northflank.com/docs/v1/api/overview
      - type: OpenAPI
        url: https://api.northflank.com/v1/openapi.json
      - type: Getting Started
        url: https://northflank.com/docs/
      - type: Pricing
        url: https://northflank.com/pricing
    contact:
      - type: Community
        url: https://discord.gg/northflank
      - type: GitHub
        url: https://github.com/northflank
common:
  - type: Developer Experience Comparison
    url: https://thesoftwarescout.com/heroku-vs-railway-vs-render-vs-fly-io-2026-which-platform-should-you-deploy-on/
  - type: PaaS Alternatives
    url: https://northflank.com/blog/best-cloud-hosting-platforms
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalable-platforms/main/json-schema/scalable-platforms-deployment-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalable-platforms/main/json-schema/scalable-platforms-serverless-function-schema.json
  - type: JSONLd
    url: https://raw.githubusercontent.com/api-evangelist/scalable-platforms/main/json-ld/scalable-platforms-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/scalable-platforms/main/vocabulary/scalable-platforms-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: kin@apievangelist.com
    url: https://apievangelist.com
include:
  - name: Scalable Infrastructure
    url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/refs/heads/main/apis.yml
  - name: Scalable Architecture
    url: https://raw.githubusercontent.com/api-evangelist/scalable-architecture/refs/heads/main/apis.yml
---
