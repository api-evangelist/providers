---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.6
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Read-only, anonymously accessible WordPress REST API served by the Alzheon corporate site at https://alzheon.com/wp-json. It exposes the company's press releases and in-the-news items (224 posts), sta
  name: Alzheon Content API (WordPress REST)
  slug: alzheon-content-api-wordpress-rest
artifact_total: 4
collections:
- collection_type: open
  name: Alzheon Content API (WordPress REST)
  slug: open-alzheon-content
common:
- group: company
  title: ''
  type: Website
  url: https://alzheon.com/
- group: company
  title: ''
  type: Blog
  url: https://alzheon.com/media/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://alzheon.com/feed/
- group: company
  title: ''
  type: News
  url: https://alzheon.com/media/in-the-news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alzheon.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://alzheon.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://alzheon.com/careers/
- group: company
  title: ''
  type: About
  url: https://alzheon.com/people/about-us/
- group: other
  title: ''
  type: Pipeline
  url: https://alzheon.com/science/pipeline/
- group: other
  title: ''
  type: Publications
  url: https://alzheon.com/science/publications/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alzheon
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Alzheon
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/alzheon_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alzheon-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alzheon-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alzheon-llms.txt
created: '2026-07-31'
description: Alzheon, Inc. is a privately held clinical-stage biopharmaceutical company founded in 2013 and headquartered at 111 Speen Street, Framingham, Massachusetts, developing oral small-molecule therapeutics and diagnostics for Alzheimer's disease and other neurodegenerative disorders. Its lead candidate, valiltramiprosate (ALZ-801) — a valine-conjugated prodrug of tramiprosate that blocks the formation of neurotoxic soluble beta-amyloid oligomers — has FDA Fast Track designation and completed the pivotal APOLLOE4 Phase 3 trial in APOE4/4 homozygotes with early Alzheimer's disease. Alzheon operates no product or developer API and publishes no developer portal, SDKs or API documentation; its corporate site does serve the standard WordPress REST API anonymously, which makes its press releases, science pages and media library machine-readable.
image: https://alzheon.com/wp-content/uploads/2016/03/alzheon-logo2.svg
layout: provider
modified: '2026-07-31'
name: Alzheon
nav: Providers
network: true
overview: 'Alzheon publishes 1 API on the [APIs.io](https://apis.io/) network: Content API (WordPress REST). Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Alzheon''s developer surface includes engineering blog, product news, and 15 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 25.8
  delta: 1.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 56.6
    developer_ergonomics: 4.2
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 24.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/screenshots/alzheon-2026-08-07T161303.png
security:
- kind: authentication
  name: Alzheon Authentication
  slug: alzheon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alzheon Domain Security
  slug: alzheon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alzheon
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Alzheimer's Disease
- Neurology
- Drug Development
- Healthcare
- Private Company
website: https://alzheon.com/
---
