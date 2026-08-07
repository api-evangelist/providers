---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: Axena Health ships Leva only as an FDA-cleared prescription end-user product — there is no developer portal, no API reference, no SDK and no GitHub org; the only machine-readable surfaces on either host are the default WordPress REST API and a WordPress MCP Adapter on levacares.com that answers tools/list with 401 mcp_unauthorized.
  evidence:
  - status: 404
    url: https://axenahealth.com/openapi.json
  - status: 401
    url: https://levacares.com/wp-json/mcp/mcp-oauth-server
  - status: 200
    url: https://levacares.com/.well-known/oauth-authorization-server
  - status: 404
    url: https://api.github.com/orgs/axenahealth
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Axena Health, Inc. is a Waltham, Massachusetts women''s health medical device company whose flagship product is the Leva Pelvic Health System, an FDA-cleared prescription digital therapeutic that pairs a vaginal motion sensor with a mobile app to deliver supervised pelvic floor muscle training for stress, mixed and mild-to-moderate urgency urinary incontinence and chronic fecal incontinence. Leva is prescribed by clinicians, dispensed to patients through telehealth and specialty channels, and is reimbursed through commercial health plans and federal channels including the Veterans Health Administration. Axena Health ships software only as a regulated end-user product: as of this profile it operates no developer portal, no public API reference, no SDKs and no partner integration program. The only machine-readable surfaces reachable without credentials are the default WordPress REST API on its two marketing sites and an OAuth-protected WordPress MCP Adapter endpoint on levacares.com.'
image: https://axenahealth.com/wp-content/uploads/cropped-AxenaSquare-e1713986234486.jpg
layout: provider
modified: '2026-08-06'
name: Axena Health
nav: Providers
network: true
random_paper: 70
slug: axena-health
tags:
- Company
- Health
- Digital Health
- Medical Devices
- Women's Health
- Digital Therapeutics
- Pelvic Health
- Medical Software
- Telehealth
---
