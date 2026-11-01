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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/cloudapper/conformance/cloudapper-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudapper-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cloudapper/llms/cloudapper-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudapper-llms.txt
- group: other
  href: https://artifacts.apis.io/cloudapper/hosts/cloudapper-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudapper-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudapper.ai/privacy-policy
- group: auth
  href: https://artifacts.apis.io/cloudapper/security/cloudapper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudapper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudapper.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.cloudapper.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.cloudapper.ai/contact-us/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cloudapper.ai/
created: '2026-10-20'
description: CloudApper provides a no-code/low-code AI‑powered platform that modernizes legacy enterprise applications across industries such as healthcare, retail, finance, and manufacturing. Their solutions include HR automation, iPaaS integration, conversational AI, and FedRAMP‑ready cloud services, enabling organizations to build, extend, and personalize apps without writing code.
image: https://www.cloudapper.ai/wp-content/uploads/2026/09/cloudapper-ai-modernize-legacy-build-enterprise-apps.jpg
layout: provider
modified: '2026-10-20'
name: CloudApper
nav: Providers
network: true
overview: 'CloudApper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, No-Code, Low-Code, and Enterprise.


  CloudApper''s developer surface includes engineering blog, support, documentation, and 6 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudapper Domain Security
  slug: cloudapper-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudapper
tags:
- Company
- AI
- No-Code
- Low-Code
- Enterprise
website: https://cloudapper.ai/
---
