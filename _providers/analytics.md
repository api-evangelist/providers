---
artifact_total: 0
coverage:
  checked: '2026-08-13'
  detail: '"Analytics" is not a company — it is a curated topical index of the analytics ecosystem published by API Evangelist, so apis.yml carries an empty apis[] with no baseURL, no humanURL and no OpenAPI servers[] host; the only host it names is the publisher''s own site (apievangelist.com), whose one real discovery document (/.well-known/api-catalog) describes API Evangelist''s agent-skills index and belongs to the separate all/api-evangelist profile, not to this index. The 21 member platforms it points at each carry their own profiles and contracts.'
  evidence:
  - status: 404
    url: https://apievangelist.com/openapi.json
  - status: 404
    url: https://apievangelist.com/.well-known/security.txt
  - status: 404
    url: https://apievangelist.com/.well-known/agent-card.json
  - status: 200
    url: https://apievangelist.com/.well-known/api-catalog
  - status: 404
    url: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/apis.yml
  reason: not-a-software-company
  state: none
layout: provider
name: analytics
nav: Providers
network: true
random_paper: 0
slug: analytics
---
