---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bttn-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bttn-llms.txt
- group: company
  title: ''
  type: Website
  url: https://bttnusa.com/
- group: company
  title: ''
  type: Blog
  url: https://bttnusa.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://bttnusa.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://bttnusa.com/faqs/
- group: company
  title: ''
  type: About
  url: https://bttnusa.com/about-us/
- group: start
  title: ''
  type: SignUp
  url: https://bttnusa.com/register
- group: start
  title: ''
  type: Login
  url: https://bttnusa.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bttnusa.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bttnusa.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bttn-usa/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/bttnusa
coverage:
  checked: '2026-08-08'
  detail: bttn sells medical supplies through a buyer-facing BigCommerce/Catalyst storefront at bttnusa.com with no developer section anywhere in its sitemap, and the host answers 200 with the same HTML catch-all for /openapi.json, /llms.txt, /graphql and every /.well-known/* path, identical to a control path that cannot exist.
  evidence:
  - status: 200
    url: https://www.bttnusa.com/zzz-nonexistent-ae-probe
  - status: 404
    url: https://www.bttnusa.com/api-docs
  - status: 404
    url: https://www.bttnusa.com/api
  - status: 200
    url: https://www.bttnusa.com/.well-known/agent-card.json
  - status: 200
    url: https://store-miy8j1e3ug-1.mybigcommerce.com/xmlsitemap.php?type=pages&page=1
  reason: no-developer-program
  state: none
created: '2026-08-08'
description: bttn (bttn Inc., trading online as bttnusa.com) is a Seattle, Washington based business-to-business e-commerce marketplace and wholesale distributor of medical supplies, lab equipment and pharmaceuticals, selling name-brand consumables to clinics, dental, veterinary and physical-therapy practices, clinical laboratories, home-healthcare providers and other healthcare buyers across the United States. Founded in 2021 by JT Garwood and Jack Miller and backed by Tiger Global, the company operates a self-serve online storefront carrying 60,000+ catalog products with bulk and volume pricing, same- or next-business-day shipping, quote requests, purchase-order and invoice payment, shopping lists, quick-order pads and recurring reorder tooling. The storefront is a BigCommerce commerce back end fronted by a Catalyst/Next.js application. bttn publishes no public developer program, API reference, or machine-readable API contract; its e-commerce surface is buyer-facing only.
image: https://www.bttnusa.com/icon.png
layout: provider
modified: '2026-08-08'
name: bttn
nav: Providers
network: true
overview: 'bttn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Supplies, Healthcare, E-Commerce, and Marketplace.


  bttn''s developer surface includes engineering blog, support, FAQ, signup flow, and 9 more developer resources.'
random_paper: 80
score:
  band: emerging
  composite: 14.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Bttn Domain Security
  slug: bttn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bttn
tags:
- Company
- Medical Supplies
- Healthcare
- E-Commerce
- Marketplace
- Wholesale
- Distribution
- Procurement
- B2B
website: https://bttnusa.com/
---
