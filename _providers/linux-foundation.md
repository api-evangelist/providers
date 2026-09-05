---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: LFX is the Linux Foundation's developer and community platform offering insights, tooling, and project lifecycle management for open source contributors and member organizations.
  name: LFX Platform
  slug: lfx-platform
- description: Programmatic access to Linux Foundation project resources, member data, and open source ecosystem information across hosted foundations such as CNCF, OpenSSF, OpenJS, LF Networking, LF Decentralized T
  name: Linux Foundation Projects
  slug: linux-foundation-projects
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linux-foundation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linux-foundation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-linux-foundation
- group: docs
  title: ''
  type: Documentation
  url: https://www.linuxfoundation.org/projects
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/LF-Engineering
- group: company
  title: ''
  type: Website
  url: https://www.linuxfoundation.org/
created: '2026-03-16'
description: The Linux Foundation is a nonprofit technology consortium that supports open source projects and ecosystems. It provides a neutral home for collaboration on open source software, hardware, standards, and data, and hosts hundreds of projects including the Linux kernel, Kubernetes, Node.js, PyTorch, OpenSSF, CNCF, RISC-V, and FINOS. The LFX platform offers tooling and insights for open source contributors and member organizations.
finops:
- name: Linux Foundation Finops
  service_category: API
  slug: linux-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linux-foundation.png
layout: provider
modified: '2026-07-25'
name: Linux Foundation
nav: Providers
network: true
overview: 'Linux Foundation publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Linux Foundation, Non-Profit, Open-Source, Technology, and LFX.


  Linux Foundation''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Linux Foundation Plans Pricing
  plan_count: 3
  slug: linux-foundation-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Linux Foundation Rate Limits
  slug: linux-foundation-rate-limits
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 12.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linux-foundation/refs/heads/main/screenshots/linux-foundation-2026-06-20T184551.png
security:
- kind: domain-security
  name: Linux Foundation Domain Security
  slug: linux-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Linux Foundation Vulnerability Disclosure
  slug: linux-foundation-vulnerability-disclosure
  summary_line: disclosure policy published
slug: linux-foundation
tags:
- Linux Foundation
- Non-Profit
- Open-Source
- Technology
- LFX
website: https://www.linuxfoundation.org/
---
