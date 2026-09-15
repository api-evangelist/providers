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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-09-14'
api_count: 1
apis:
- baseURL: https://www.synsense.ai/wp-json
  baseurl_source: declared
  description: 'The public WordPress REST API served at https://www.synsense.ai/wp-json. Fully anonymous and read-only for the content surface, it exposes SynSense''s own custom post types as JSON — products, partner '
  name: SynSense Website Content API
  slug: website-content-api
artifact_total: 6
common:
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
created: '2026-09-14'
description: 'aiCTX AG — renamed SynSense AG in May 2020 — is a neuromorphic computing company founded in Zurich in 2017 out of the Institute of Neuroinformatics at the University of Zurich and ETH Zurich. It designs ultra-low-power mixed-signal neuromorphic processors and smart sensors for always-on, sub-milliwatt edge inference: the Speck and DYNAP-CNN event-driven vision SoCs, the Xylo family for audio and IMU signal processing, and the DVS, Rigi and AEVEON sensor series. Its developer surface is a stack of open-source Python libraries rather than a product web API — Samna (the device interface and runtime), Rockpool (spiking network training and deployment) and Sinabs (PyTorch spiking CNNs) — backed by a developer community, forum, and firmware and datasheet download hub at synsense.ai. The one HTTP API the company serves publicly is the anonymous, read-only WordPress REST content API behind that corporate site, which exposes its products, partners, offices, awards, open roles and news
  as machine-readable JSON.'
examples:
- key_count: 13
  name: Aictx Content Types
  slug: aictx-content-types
image: https://www.synsense.ai/wp-content/uploads/2022/03/logo-synsense-blue.svg
layout: provider
modified: '2026-09-14'
name: aiCTX (now SynSense)
nav: Providers
network: true
overview: 'aiCTX (now SynSense) publishes 1 API on the [APIs.io](https://apis.io/) network: SynSense Website Content API. Tagged areas include Company, Neuromorphic Computing, Artificial Intelligence, Semiconductors, and Edge Computing.


  aiCTX (now SynSense)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, and 17 more developer resources.'
plans:
- name: Aictx Plans Pricing
  plan_count: 0
  slug: aictx-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Aictx Rate Limits
  slug: aictx-rate-limits
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 57.8
    developer_ergonomics: 66.1
    discoverability: 68.5
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
- Machine-Learning
- Sensors
- Internet of Things
- Open-Source
- Content
website: https://www.synsense.ai/
---
