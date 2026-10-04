---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
- description: 'The public WordPress REST API (wp-json) of the Allay Therapeutics website at www.allaytx.com: the route index of the site''s content management system, catalogued as one site surface rather than as sep'
  name: Allay Therapeutics Website (WordPress REST)
  slug: allaytx-com-website-wordpress-rest
artifact_total: 4
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/overlays/allay-therapeutics-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/allay-therapeutics-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.allaytx.com/
- group: company
  title: ''
  type: About
  url: https://www.allaytx.com/about-us/
- group: other
  title: ''
  type: Science
  url: https://www.allaytx.com/our-science/
- group: other
  title: ''
  type: Pipeline
  url: https://www.allaytx.com/pipeline/
- group: company
  title: ''
  type: News
  url: https://www.allaytx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.allaytx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.allaytx.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.allaytx.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allaytx.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allaytx.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allaytx/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/allaytx
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/authentication/allay-therapeutics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allay-therapeutics-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/conventions/allay-therapeutics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/allay-therapeutics-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/conformance/allay-therapeutics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allay-therapeutics-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/errors/allay-therapeutics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/allay-therapeutics-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/lifecycle/allay-therapeutics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/allay-therapeutics-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/data-model/allay-therapeutics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allay-therapeutics-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/well-known/allay-therapeutics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allay-therapeutics-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/security/allay-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allay-therapeutics-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/llms/allay-therapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allay-therapeutics-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: Allay Therapeutics is a clinical-stage biopharmaceutical company with operations in San Jose, California and Singapore, developing ultra-sustained, non-opioid analgesic products for post-surgical pain management. Its platform is a tunable drug-biopolymer architecture that pairs validated non-opioid analgesics with dissolvable biopolymers to release pain relief at a targeted surgical site over weeks rather than days, and can be tuned for constant release (chronic pain such as osteoarthritis) or pulsed release (cyclic pain such as gout). Lead candidate ATX-101 is a bupivacaine-based implant placed directly at the surgical site during total knee replacement (TKA), targeting the three-day to two-week analgesia gap that drives breakthrough pain and opioid use; it holds FDA Breakthrough Therapy Designation and entered a pivotal Phase 2b registration trial with first patients dosed in 2025. Additional programs (ATX-201, ATX-301, ATX-401, ATX-501) span new formulations, injectables,
  additional clinical indications and on-demand anesthetic delivery. The company raised a $57.5M Series D plus a venture debt line in 2025 and has a development and commercialization agreement with Maruishi Pharmaceutical for Japan. It is a therapeutics developer, not a software company, and publishes no developer program, API, SDK, or machine-readable interface.
image: https://www.allaytx.com/wp-content/uploads/2021/04/brand-allay.png
layout: provider
modified: '2026-08-06'
name: Allay Therapeutics
nav: Providers
network: true
overview: 'Allay Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Pain Management, and Drug Delivery.


  Allay Therapeutics'' developer surface includes product news, authentication, and 22 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 16.3
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/screenshots/allay-therapeutics-2026-08-07T161209.png
security:
- kind: authentication
  name: Allay Therapeutics Authentication
  slug: allay-therapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Allay Therapeutics Domain Security
  slug: allay-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allay-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Pain Management
- Drug Delivery
- Non-Opioid
- Clinical Stage
- Health
- Life Sciences
- content-api
website: https://www.allaytx.com/
---
