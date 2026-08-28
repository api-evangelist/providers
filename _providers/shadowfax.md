---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-27'
  detail: 'Shadowfax AI ships its agentic-analytics platform only as an end-user web application: the 35-page Docusaurus documentation site has no API reference section, the pricing tiers name no API allowance, github.com/shadowfax-ai has zero public repositories, and the only HTTP contract on any host is the SPA backend route app.shadowfax.ai/openapi.json, which is not a product API and answers unauthenticated callers with a Clerk session-token 401.'
  evidence:
  - status: 401
    url: https://app.shadowfax.ai/openapi.json
  - status: 200
    url: https://docs.shadowfax.ai/sitemap.xml
  - status: 404
    url: https://shadowfax.ai/api
  - status: 404
    url: https://shadowfax.ai/llms.txt
  - status: 404
    url: https://shadowfax.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-27'
description: 'Shadowfax AI is an AI-native, agentic analytics platform founded in 2025 and based in Menlo Park, California, built by veterans of Snowflake, Palantir, Rubrik and Alteryx and backed by Khosla Ventures and the Snowflake Startup Accelerator. The product combines a spreadsheet, a BI tool, a visual pipeline and a code notebook into one analyst-in-the-loop workflow: users upload CSV, TSV, Excel or Parquet sources, which are held immutable, and every transformation produces a new View with full lineage, inspectable SQL and an auditable node graph. Features include AI Tables, an AI chat interface, schema discovery, slash commands, a reactive dependency system, manual SQL mode and a Vega-based visualization framework. It is in free public beta; live database connections to Snowflake and BigQuery are announced as coming soon. Shadowfax AI publishes no public developer API — the platform is an end-user product and its only HTTP contract sits behind a Clerk-authenticated session on app.shadowfax.ai.'
image: https://docs.shadowfax.ai/img/shadowfax-social-card.png
layout: provider
modified: '2026-08-27'
name: Shadowfax AI
nav: Providers
network: true
random_paper: 20
slug: shadowfax
tags:
- Company
- Analytics
- Business Intelligence
- Artificial Intelligence
- Data
- Agentic Analytics
- Data Engineering
- SaaS
---
