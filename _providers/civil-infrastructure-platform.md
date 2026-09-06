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
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: 'The CIP Kernel is a Super Long-Term Support (SLTS) Linux kernel branch maintained for ten or more years, providing a stable base for industrial systems that must remain in service across multi-decade '
  name: CIP SLTS Kernel
  slug: cip-kernel
- description: CIP Core provides a curated set of Debian-derived user-space packages aligned with the SLTS kernel to deliver a complete reference platform for civil infrastructure devices.
  name: CIP Core Packages
  slug: cip-core
- description: The CIP Software Update working group maintains tooling such as SWUpdate and hawkBit-based servers used to deliver secure over-the-air updates across long-lived industrial deployments.
  name: CIP Software Update
  slug: cip-software-update
- description: The CIP Security working group aligns the CIP base layer with IEC 62443-4-1 and 62443-4-2 industrial cybersecurity requirements and tracks CVE handling across the SLTS kernel and user-space.
  name: CIP Security
  slug: cip-security
- description: The CIP Testing working group runs continuous-integration and hardware-in-the-loop testing on member-supplied boards to validate kernel and core packages against the SLTS branch.
  name: CIP Testing
  slug: cip-testing
- baseURL: https://cip-project.org/wp-json/tec/v1
  baseurl_source: declared
  description: 'The only live, callable REST API the Civil Infrastructure Platform serves: the community event calendar behind cip-project.org/events, exposing events, venues, organizers and series. Published reads a'
  name: CIP Events REST API
  slug: cip-events-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/civil-infrastructure-platform-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/civil-infrastructure-platform-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/civil-infrastructure-platform
- group: company
  title: ''
  type: Website
  url: https://www.cip-project.org/
- group: other
  title: ''
  type: Wiki
  url: https://wiki.linuxfoundation.org/civilinfrastructureplatform
- group: build
  title: ''
  type: GitLab
  url: https://gitlab.com/cip-project
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cip-project
- group: other
  title: ''
  type: Mailing List
  url: https://lists.cip-project.org/g/cip-dev
- group: design
  title: ''
  type: JSONLD
  url: json-ld/civil-infrastructure-platform-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/civil-infrastructure-platform-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://cip-project.org/blog/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/civil-infrastructure-platform-tec-v1-openapi-original.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/civil-infrastructure-platform-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://www.cip-project.org/.well-known/api-catalog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/civil-infrastructure-platform-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/civil-infrastructure-platform-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/civil-infrastructure-platform-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/civil-infrastructure-platform-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/civil-infrastructure-platform-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/civil-infrastructure-platform-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bestpractices.dev/projects/10564
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/civil-infrastructure-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://wiki.linuxfoundation.org/civilinfrastructureplatform/cipkernelmaintenance#security_fixes
- group: build
  title: ''
  type: Packages
  url: packages/civil-infrastructure-platform-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/civil-infrastructure-platform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/civil-infrastructure-platform-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/civil-infrastructure-platform-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://cip-documents.readthedocs.io/
- group: operate
  title: ''
  type: Support
  url: https://lists.cip-project.org/g/cip-dev
- group: commercial
  title: ''
  type: Pricing
  url: https://cip-project.org/about/join
- group: start
  title: ''
  type: SignUp
  url: https://enrollment.lfx.linuxfoundation.org/?project=cip
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/privacy
- group: company
  title: ''
  type: BlogRSS
  url: https://cip-project.org/feed
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cip_project
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/civil-infrastructure-platform-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/civil-infrastructure-platform-mcp.yml
- group: docs
  title: ''
  type: APIReference
  url: https://cip-project.org/wp-json/tec/v1/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cip-project
created: '2026-03-16'
description: 'The Civil Infrastructure Platform (CIP) is a Linux Foundation collaborative project that builds an industrial-grade open source base layer for civil infrastructure systems such as transportation, power generation and distribution, building and city management, industrial control, and healthcare equipment. CIP curates a Super Long-Term Support (SLTS) kernel and core user-space packages that can be maintained for more than ten years, plus working groups for security (IEC 62443 alignment), software update, real-time, and testing. CIP''s primary programmable interface is source code — the kernel, CIP Core images and tooling published through GitLab and Debian-derived package archives — and it publishes machine-readable product lifecycle data for those. CIP also serves one live REST API: its own event calendar at cip-project.org/wp-json, declared in an RFC 9727 /.well-known/api-catalog and described by OpenAPI documents the site serves itself.'
finops:
- name: Civil Infrastructure Platform Finops
  service_category: API
  slug: civil-infrastructure-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/civil-infrastructure-platform.png
jsonld:
- class_count: 13
  name: Civil Infrastructure Platform Context
  property_count: 0
  slug: civil-infrastructure-platform-context
layout: provider
modified: '2026-09-05'
name: Civil Infrastructure Platform
nav: Providers
network: true
overview: 'Civil Infrastructure Platform publishes 1 API on the [APIs.io](https://apis.io/) network: CIP Events REST API. Tagged areas include Embedded, Industrial, Infrastructure, Linux, and Linux Foundation.


  The Civil Infrastructure Platform catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Civil Infrastructure Platform''s developer surface includes authentication, GitHub presence, engineering blog, documentation, support, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Civil Infrastructure Platform Plans Pricing
  plan_count: 0
  slug: civil-infrastructure-platform-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Civil Infrastructure Platform Rate Limits
  slug: civil-infrastructure-platform-rate-limits
rules:
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Civil Infrastructure Platform API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: civil-infrastructure-platform-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.0
    catalog_earned_first_party: 0.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 31.2
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 63.6
    contract_quality: 65.8
    developer_ergonomics: 37.5
    discoverability: 83.3
    governance: 63.6
    operational_transparency: 28.9
  previous_composite: 21.9
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/civil-infrastructure-platform/refs/heads/main/screenshots/civil-infrastructure-platform-2026-06-20T174430.png
security:
- kind: authentication
  name: Civil Infrastructure Platform Authentication
  slug: civil-infrastructure-platform-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Civil Infrastructure Platform Domain Security
  slug: civil-infrastructure-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Civil Infrastructure Platform Vulnerability Disclosure
  slug: civil-infrastructure-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: civil-infrastructure-platform
tags:
- Embedded
- Industrial
- Infrastructure
- Linux
- Linux Foundation
- Long-Term Support
- Open-Source
website: https://www.cip-project.org/
---
