---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cosm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cosm.com/
- group: company
  title: ''
  type: About
  url: https://www.cosm.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.cosm.com/news
- group: operate
  title: ''
  type: Support
  url: https://help.cosm.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cosm.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cosm.com/legal/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.cosm.com/careers
- group: other
  title: ''
  type: TechnologySite
  url: https://tech.cosm.com/
- group: start
  title: ''
  type: PartnerPortal
  url: https://partners.cosm.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/experiencecosm/
- group: other
  title: ''
  type: X
  url: https://x.com/experiencecosm
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cosm-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cosm-llms.txt
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
overview: 'Cosm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Immersive Experiences, Entertainment, Media, and Sports.


  Cosm''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Cosm Plans Pricing
  plan_count: 0
  slug: cosm-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Cosm Rate Limits
  slug: cosm-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Cosm Domain Security
  slug: cosm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
website: https://www.cosm.com/
---
