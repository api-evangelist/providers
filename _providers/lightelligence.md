---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lightelligence.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.lightelligence.ai/about-us/news/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.lightelligence.ai/about-us/contact-us
- group: operate
  title: ''
  type: Community
  url: https://www.lightelligence.ai/community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lightelligence
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lightelligence.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lightelligence.ai/legal
- group: build
  title: ''
  type: Packages
  url: packages/lightelligence-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightelligence-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/lightelligence-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lightelligence-rate-limits.yml
coverage:
  checked: '2026-08-25'
  detail: Lightelligence sells optoelectronic hardware (PCIe accelerator cards, optical switches) with no hosted API at all, and the one developer program it did run has been taken down — the lightelligence-sdk PyPI package, its Read the Docs reference and the Lightelligence/SDKDocs repository all 404 while the company's own public SDKExamples repo still tells users to install them.
  evidence:
  - status: 404
    url: https://pypi.org/simple/lightelligence-sdk/
  - status: 404
    url: https://lightelligence-sdk.readthedocs.io/en/latest/index.html
  - status: 404
    url: https://api.github.com/repos/Lightelligence/SDKDocs
  - status: 404
    url: https://www.lightelligence.ai/openapi.json
  - status: 404
    url: https://www.lightelligence.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Lightelligence (legal entity Shanghai Xizhi Technology Co., Ltd. / 曦智科技, founded 2017 as an MIT spin-out) builds optoelectronic hybrid computing hardware — photonic accelerators and optical interconnect fabric for AI and high-performance computing. Its product line is physical: the PACE 2 optoelectronic accelerated computing card (a PCIe Gen4 x16 accelerator built around a 128x128 optical matrix multiplier), the Gazelle optical computing evaluation board, the Photowave CXL optical interconnect, and the Lightsphere X distributed optical circuit switch, supported by the company''s oMAC, oNOC and oNET optical core, network-on-chip and inter-chip network technologies. The software surface is a device-side stack — ONNX, OpenCL, PyTorch and TVM support plus a Python SDK (lt_sdk) that compiled and ran models on the optical processing unit — not a web API. As of this profile the company publishes no public web API, no OpenAPI/AsyncAPI/GraphQL contract, and no developer portal; the
  lightelligence-sdk package and its Read the Docs reference have both been withdrawn. Its remaining public developer-facing surface is a GitHub organization of chip design and verification tooling (Bazel Verilog build rules, RTL/UVM linters, the yis interface-spec generator) and an Optical Computing Developer Community of research cases and papers.'
image: https://www.lightelligence.ai/Public/Uploads/uploadfile/images/20260622/logoen.png
layout: provider
modified: '2026-08-25'
name: Lightelligence
nav: Providers
network: true
overview: 'Lightelligence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Optical Computing, Photonics, Semiconductors, and AI Infrastructure.


  Lightelligence''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Lightelligence Plans Pricing
  plan_count: 0
  slug: lightelligence-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Lightelligence Rate Limits
  slug: lightelligence-rate-limits
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightelligence/refs/heads/main/screenshots/lightelligence-2026-09-02T150252.png
security:
- kind: domain-security
  name: Lightelligence Domain Security
  slug: lightelligence-domain-security
  summary_line: TLSv1.3
slug: lightelligence
tags:
- Company
- Optical Computing
- Photonics
- Semiconductors
- AI Infrastructure
- Hardware Accelerators
- High Performance Computing
- Optical Interconnect
- Data-Center
website: https://www.lightelligence.ai/
---
