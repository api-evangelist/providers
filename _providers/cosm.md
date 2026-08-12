---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-11'
  detail: Cosm markets exactly one API — Digistar's, advertised on tech.cosm.com as "the most fully featured API across the planetarium industry" — and its only documentation link, the Access Portal at support.es.com (TLS certificate expired, http meta-refresh), lands on a Salesforce Experience Cloud login at partners.cosm.com where every path but OIDC discovery answers 401.
  evidence:
  - status: 200
    url: https://tech.cosm.com/products/digistar-projection-system/digistar
  - status: 200
    url: https://support.es.com/
  - status: 301
    url: https://partners.cosm.com/
  - status: 401
    url: https://partners.cosm.com/openapi.json
  - status: 404
    url: https://www.cosm.com/llms.txt
  reason: partner-login
  state: gated
created: '2026-08-11'
description: 'Cosm is a Los Angeles-based immersive technology, media and entertainment company formed in 2020 from the merger of LiveLike VR (now Cosm Immersive) and C360, followed by the acquisition of planetarium pioneers Evans & Sutherland and Spitz. It operates three lines: Cosm Tech (the CX System LED dome, Digistar planetarium software, and end-to-end immersive display systems sold to planetariums, museums and attractions), Cosm Media (immersive content production and licensing through Cosm Studios) and Cosm Venues (the "Shared Reality" experiential venues in Los Angeles and Dallas, with Atlanta, Detroit and Cleveland following). Cosm sells and operates systems and venues rather than a developer platform: it publishes no public API, SDK, developer portal or machine-readable specification. The one API it markets — the Digistar scripting/automation interface, advertised as "the most fully featured API across the planetarium industry" — is documented only inside the customer support
  portal at partners.cosm.com, which requires a login.'
image: https://prod.cosm-cdn.io/cosmdotcom/content_pages/cosm/cosm-we-power-immersive-experiences-around-the-world.webp
layout: provider
modified: '2026-08-11'
name: Cosm
nav: Providers
network: true
random_paper: 86
slug: cosm
tags:
- Company
- Immersive Experiences
- Entertainment
- Media
- Sports
- Venues
- Display Technology
- Planetarium
- Content Production
---
