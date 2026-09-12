---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: AgentSquared's domain agentsquared.com was re-registered in February 2026 and now serves an unrelated online-casino affiliate site (the WordPress discovery document at https://agentsquared.com/wp-json/ names the site "Online Casinos"), every page of the former real estate site returns 404, the customer login host dashboard.agentsquared.com no longer resolves, and STEP 0b contract discovery against both surviving hosts — /openapi.json, /swagger.json, /api-docs, /llms.txt, /apis.json and the full /.well-known/ set including agent-card.json and agent.json — returned only 403 Cloudflare interstitials and 404s, which is consistent with the company never having published a developer portal, API reference or machine-readable contract while it operated (it was a RESO Web API consumer, not a producer).
  evidence:
  - status: 403
    url: https://www.agentsquared.com/
  - status: 200
    url: https://agentsquared.com/wp-json/
  - status: 200
    url: https://agentsquared.com/page-sitemap.xml
  - status: 404
    url: https://www.agentsquared.com/pricing/
  - status: 404
    url: https://www.agentsquared.com/support/
  - status: 404
    url: https://www.agentsquared.com/how-it-works/
  - status: 404
    url: https://www.agentsquared.com/mls-partners/
  - status: 0
    url: https://dashboard.agentsquared.com/login/auth/login
  - status: 403
    url: https://www.agentsquared.com/openapi.json
  - status: 404
    url: https://www.agentsquared.com/llms.txt
  - status: 404
    url: https://www.agentsquared.com/.well-known/agent-card.json
  - status: 404
    url: https://www.agentsquared.com/.well-known/security.txt
  - status: 404
    url: https://registry.npmjs.org/agentsquared
  - status: 404
    url: https://pypi.org/pypi/agentsquared/json
  - status: 200
    url: https://www.linkedin.com/company/agentsquared/
  - status: 200
    url: https://equityzen.com/company/agentsquared
  reason: defunct
  state: none
created: '2026-09-12'
description: 'AgentSquared was a La Jolla, California real estate marketing technology company, founded in 2013 by Albert Lopez and a team its LinkedIn page describes as "Internet pioneers who have founded, built and sold leading brand name Internet companies such as Media Temple, Miva, and Attracta." Its product was marketing automation for real estate agents and brokers: Instant IDX websites provisioned with a single click, single-property websites generated automatically for new listings, social sharing of those listings, lead capture and CRM, and Google Business Profile and Local Services Ads management. The company was notable as an API CONSUMER rather than an API producer — it was a RESO (Real Estate Standards Organization) member and one of the few vendors building on the National Association of Realtors Web API standard, using deep integrations and channel partnerships with MLS software providers to pull a broker''s identity and listing data straight out of the MLS and stand up a
  fully populated website from it. It worked with RESO to help define and document the client portion of the RESO Web API certification program. AgentSquared never published a developer program of its own: no developer portal, API reference, OpenAPI or other machine-readable contract, SDK, or public package ever appeared on its site. The company reached roughly $961K in reported revenue without raising venture capital. Its web presence is now gone — see x-status below.'
layout: provider
modified: '2026-09-12'
name: AgentSquared
nav: Providers
network: true
random_paper: 3
slug: agentsquared
tags:
- Company
- Real Estate
- Real Estate Technology
- Marketing Automation
- MLS
- IDX
- RESO
- Lead Generation
- Website Builder
- Defunct
---
