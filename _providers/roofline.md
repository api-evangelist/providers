---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.roofline.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.roofline.ai/news
- group: operate
  title: ''
  type: Support
  url: https://www.roofline.ai/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.roofline.ai/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RooflineAI
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.roofline.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/roofline-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/roofline-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/roofline-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roofline-domain-security.yml
coverage:
  checked: '2026-08-17'
  detail: All three Roofline products — SDK, Runtime and Performance Dashboard — end at the same sentence, "Just reach out through our Contact Us form", and the only "view docs" link on those pages resolves to github.com/RooflineAI, an org whose own profile README disclaims its repos as "not a Roofline AI product".
  evidence:
  - status: 200
    url: https://www.roofline.ai/product-sdk
  - status: 200
    url: https://www.roofline.ai/contact-us
  - status: 404
    url: https://www.roofline.ai/pricing
  - status: 404
    url: https://www.roofline.ai/openapi.json
  - status: 404
    url: https://www.roofline.ai/.well-known/agent-card.json
  - status: 0
    url: https://docs.roofline.ai/
  reason: sales-gate
  state: gated
created: '2026-08-17'
description: 'Roofline (RooflineAI GmbH, Köln, Germany) is a 2024 RWTH Aachen University spin-off building a retargetable AI compiler stack for edge deployment. Its three products are an SDK that compiles models ahead of time from any framework — the product page shows a single Python call, attic.compile(model, (input,)) — a lightweight C runtime with Python bindings that executes the compiled model and orchestrates heterogeneous SoCs, and a Performance Dashboard fed by a roofbench command-line tool running nightly benchmarks across hundreds of models for latency, throughput and memory footprint. The stack is built on open-source MLIR and IREE with proprietary hardware-specific optimization on top, and targets NPUs, MCUs and heterogeneous SoCs with quantization (INT8, blocked, symmetric, asymmetric, dynamic), dynamic shapes for on-device LLMs and mixture-of-experts support. Published work includes NXP eIQ Neutron NPU LLM enablement, Vulkan 1.3 and Arm SVE support in IREE, and day-0 support
  for Liquid AI LFM2. Roofline is a strategic partner of the Edge AI Foundation and raised a seed round from Serena and First Momentum Ventures. It sells compiler licenses to hardware vendors and embedded software teams: there is no developer program, no public API, no documentation host and no registry-published package. Every product page ends at a Contact Sales form, and the only machine-readable document Roofline publishes anywhere is an llms.txt on its marketing site.'
image: https://cdn.prod.website-files.com/691c3b22c31ce2676bca90d5/691c3b22c31ce2676bca9100_roofline.svg
layout: provider
modified: '2026-08-17'
name: Roofline
nav: Providers
network: true
overview: 'Roofline is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Edge AI, AI Compiler, and MLIR.


  Roofline''s developer surface includes engineering blog, support, signup flow, and 7 more developer resources.'
plans:
- name: Roofline Plans Pricing
  plan_count: 0
  slug: roofline-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/roofline/refs/heads/main/screenshots/roofline-2026-09-02T154110.png
security:
- kind: domain-security
  name: Roofline Domain Security
  slug: roofline-domain-security
  summary_line: TLSv1.3 · HSTS
slug: roofline
tags:
- Company
- Ai Data
- Edge AI
- AI Compiler
- MLIR
- IREE
- Machine-Learning
- Model Deployment
- Embedded
- NPU
- Quantization
- On-Device LLM
- Developer Tools
- Germany
website: https://www.roofline.ai/
---
