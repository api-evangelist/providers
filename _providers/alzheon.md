---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.1
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Alzheon website at alzheon.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Alzheon Website (WordPress REST)
  slug: alzheon-com-website-wordpress-rest
artifact_total: 3
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
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/well-known/alzheon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alzheon-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/security/alzheon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alzheon-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/llms/alzheon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alzheon-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/authentication/alzheon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alzheon-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/conventions/alzheon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alzheon-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/errors/alzheon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alzheon-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/data-model/alzheon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alzheon-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/lifecycle/alzheon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alzheon-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alzheon/refs/heads/main/conformance/alzheon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alzheon-conformance.yml
created: '2026-07-31'
description: Alzheon, Inc. is a privately held clinical-stage biopharmaceutical company founded in 2013 and headquartered at 111 Speen Street, Framingham, Massachusetts, developing oral small-molecule therapeutics and diagnostics for Alzheimer's disease and other neurodegenerative disorders. Its lead candidate, valiltramiprosate (ALZ-801) — a valine-conjugated prodrug of tramiprosate that blocks the formation of neurotoxic soluble beta-amyloid oligomers — has FDA Fast Track designation and completed the pivotal APOLLOE4 Phase 3 trial in APOE4/4 homozygotes with early Alzheimer's disease. Alzheon operates no product or developer API and publishes no developer portal, SDKs or API documentation; its corporate site does serve the standard WordPress REST API anonymously, which makes its press releases, science pages and media library machine-readable.
image: https://alzheon.com/wp-content/uploads/2016/03/alzheon-logo2.svg
layout: provider
modified: '2026-07-31'
name: Alzheon
nav: Providers
network: true
overview: 'Alzheon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Alzheon''s developer surface includes engineering blog, product news, authentication, and 20 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
- Alzheimers Disease
- Neurology
- Drug Development
- Healthcare
- Private Company
website: https://alzheon.com/
---
