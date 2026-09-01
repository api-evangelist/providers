---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advolveai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advolve.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/advolve-ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/advolve
coverage:
  checked: '2026-08-12'
  detail: Advolve sells an AI-run performance-marketing service through a five-page marketing SPA and a Cloudflare Access-protected customer console at app.advolve.ai — there is no developer portal, no API reference, no SDK and no public API host, and the only Advolve API hostname published anywhere (landing-page-api.advolve.ai, the site's own contact-form backend) no longer resolves.
  evidence:
  - status: 200
    url: https://advolve.ai/openapi.json
  - status: 200
    url: https://advolve.ai/.well-known/agent-card.json
  - status: 200
    url: https://advolve.ai/sitemap.xml
  - status: 302
    url: https://app.advolve.ai/
  - status: 0
    url: https://landing-page-api.advolve.ai/contacts
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Advolve.AI is an AI-driven performance-marketing and customer-acquisition platform for e-commerce brands and marketplaces, offering an end-to-end solution to automate, scale, and optimize paid media and digital advertising, including a patent-pending creative-optimization capability that tunes interactive ad elements (messaging, graphics, colors, fonts). Founded in 2023 and headquartered in Sao Paulo, Brazil, Advolve was backed by Prosus Ventures and Valor Capital and was acquired by iFood (Prosus group) in November 2025 to power iFood Ads across Latin America. Advolve publishes a marketing website only; as of enrichment it exposes no public developer program, API, SDKs, or documentation surface.
image: https://advolve.ai/images/og-image.png
layout: provider
modified: '2026-08-12'
name: Advolve.AI
nav: Providers
network: true
overview: Advolve.AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Advertising, Marketing, and AdTech.
plans:
- name: Advolveai Plans Pricing
  plan_count: 0
  slug: advolveai-plans-pricing
random_paper: 10
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/advolveai/refs/heads/main/screenshots/advolveai-2026-07-25T181710.png
security:
- kind: domain-security
  name: Advolveai Domain Security
  slug: advolveai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: advolveai
tags:
- Company
- Artificial Intelligence
- Advertising
- Marketing
- AdTech
- MarTech
- Performance Marketing
- E-Commerce
- Brazil
website: https://advolve.ai
---
