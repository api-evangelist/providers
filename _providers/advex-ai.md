---
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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.advexai.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdvexAI
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advex-ai-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/advex-ai-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advex-ai-llms.txt
coverage:
  checked: '2026-09-09'
  detail: Advex sells Composer as an on-premises visual-inspection appliance (the "Advex box") driven by a no-code UI and explicitly designed to run on-device without network connectivity, so it has never published an API, developer portal, SDK or machine-readable spec — its own site's entire navigation was Use Cases, Benefits, Pricing, FAQ, Blog and Book A Demo — and as of this check even that site is unpublished, answering HTTP 404 from an empty Framer origin on every host and path.
  evidence:
  - status: 404
    url: https://www.advexai.com/
  - status: 301
    url: https://advex.ai/
  - status: 404
    url: https://www.advexai.com/openapi.json
  - status: 404
    url: https://www.advexai.com/.well-known/security.txt
  - status: 200
    url: https://api.github.com/orgs/AdvexAI
  - status: 200
    url: http://web.archive.org/web/20260612174810/https://www.advexai.com/
  reason: no-developer-program
  state: none
created: '2026-09-09'
description: Advex AI (Advex AI, Inc., San Francisco / Pleasanton, California; founded 2022 by Pedro Pachuca and Qasim Wani) builds generative-AI synthetic data and self-healing computer vision for industrial quality inspection. Its flagship product, Composer, is a no-code AI vision system that lets manufacturing and logistics teams train, deploy and manage visual inspection tasks — defect and anomaly detection, pick-and-place, kitting and assembly verification, counting — from a handful of real images, using diffusion models to synthesize the missing training data and VLMs to run the inspection. Composer is sold as an on-premises appliance (the "Advex box") paired with plant cameras and is explicitly designed to run entirely on-device without network connectivity. The company raised a $3.5M seed round in November 2024 led by Construct Capital with Pear VC and Emerson Collective. As of this profile Advex publishes no public API, developer portal, SDK or machine-readable specification of
  any kind, and its own website is currently unpublished.
image: https://avatars.githubusercontent.com/u/119636653?v=4
layout: provider
modified: '2026-09-09'
name: Advex AI
nav: Providers
network: true
overview: Advex AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Computer Vision, Synthetic Data, and Manufacturing.
plans:
- name: Advex Ai Plans Pricing
  plan_count: 0
  slug: advex-ai-plans-pricing
random_paper: 6
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Advex Ai Domain Security
  slug: advex-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: advex-ai
tags:
- Company
- Artificial Intelligence
- Computer Vision
- Synthetic Data
- Manufacturing
- Machine Learning
- Quality Inspection
- Industrial Automation
website: https://www.advexai.com/
---
