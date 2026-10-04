---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the aiCTX (now SynSense) website at www.synsense.ai: the route index of the site''s content management system, catalogued as one site surface rather than as s'
  name: aiCTX (now SynSense) Website (WordPress REST)
  slug: synsense-ai-website-wordpress-rest
artifact_total: 5
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/overlays/aictx-website-content-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aictx-website-content-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.synsense.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.synsense.ai/developercommunity/
- group: docs
  title: ''
  type: Documentation
  url: https://www.synsense.ai/developercommunity/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://synsense-sys-int.gitlab.io/samna/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.synsense.ai/speck-quick-start-guide/
- group: operate
  title: ''
  type: Support
  url: https://www.synsense.ai/contact-2/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.synsense.ai/developercommunity/
- group: company
  title: ''
  type: Blog
  url: https://www.synsense.ai/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.synsense.ai/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synsense
- group: start
  title: ''
  type: Login
  url: https://www.synsense.ai/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synsense.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synsense.ai/privacy-policy/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/packages/aictx-packages.yml
  title: ''
  type: Packages
  url: packages/aictx-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/packages/aictx-packages.yml
  title: ''
  type: SDKs
  url: packages/aictx-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/llms/aictx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aictx-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/conformance/aictx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aictx-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/lifecycle/aictx-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aictx-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/changelog/aictx-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aictx-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/plans/aictx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aictx-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/security/aictx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aictx-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/well-known/aictx-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/aictx-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/authentication/aictx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aictx-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/errors/aictx-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aictx-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/conventions/aictx-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aictx-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/data-model/aictx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aictx-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/rate-limits/aictx-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aictx-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aictx/refs/heads/main/mcp/aictx-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aictx-mcp.yml
created: '2026-09-14'
description: 'aiCTX AG — renamed SynSense AG in May 2020 — is a neuromorphic computing company founded in Zurich in 2017 out of the Institute of Neuroinformatics at the University of Zurich and ETH Zurich. It designs ultra-low-power mixed-signal neuromorphic processors and smart sensors for always-on, sub-milliwatt edge inference: the Speck and DYNAP-CNN event-driven vision SoCs, the Xylo family for audio and IMU signal processing, and the DVS, Rigi and AEVEON sensor series. Its developer surface is a stack of open-source Python libraries rather than a product web API — Samna (the device interface and runtime), Rockpool (spiking network training and deployment) and Sinabs (PyTorch spiking CNNs) — backed by a developer community, forum, and firmware and datasheet download hub at synsense.ai. The one HTTP API the company serves publicly is the anonymous, read-only WordPress REST content API behind that corporate site, which exposes its products, partners, offices, awards, open roles and news
  as machine-readable JSON.'
image: https://www.synsense.ai/wp-content/uploads/2022/03/logo-synsense-blue.svg
layout: provider
modified: '2026-09-14'
name: aiCTX (now SynSense)
nav: Providers
network: true
overview: 'aiCTX (now SynSense) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Neuromorphic Computing, Artificial Intelligence, Semiconductors, and Edge Computing.


  aiCTX (now SynSense)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 23 more developer resources.'
plans:
- name: Aictx Plans Pricing
  plan_count: 0
  slug: aictx-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Aictx Rate Limits
  slug: aictx-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 30.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aictx Authentication
  slug: aictx-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aictx Domain Security
  slug: aictx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aictx
tags:
- Company
- Neuromorphic Computing
- Artificial Intelligence
- Semiconductors
- Edge Computing
- Machine Learning
- Sensors
- IoT
- Open Source
website: https://www.synsense.ai/
---
