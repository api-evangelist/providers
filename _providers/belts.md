---
artifact_total: 0
coverage:
  checked: '2026-09-19'
  detail: '"Belts" is a topical index of the conveyor-belt ecosystem, not a company: apis[] is empty and the only hosts the record names belong to the standards bodies it cites (CEMA at cemanet.org, ANSI at ansi.org), neither of which publishes a developer program or a machine-readable contract - cemanet.org 404s /openapi.json, /swagger.json, /api-docs and /llms.txt and WAF-403s every /.well-known/* path (its only 200 JSON is WordPress''s own /wp-json/ platform surface), and every ansi.org host answers a Cloudflare JS challenge (403) for every path probed.'
  evidence:
  - status: 200
    url: https://cemanet.org/
  - status: 404
    url: https://cemanet.org/openapi.json
  - status: 404
    url: https://cemanet.org/llms.txt
  - status: 403
    url: https://cemanet.org/.well-known/agent-card.json
  - status: 403
    url: https://webstore.ansi.org/industry/conveyors/belt-standards
  - status: 403
    url: https://ansi.org/.well-known/api-catalog
  reason: not-a-software-company
  state: none
layout: provider
name: belts
nav: Providers
network: true
random_paper: 10
slug: belts
---
