---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ATSPrep provides resume checking, job matching, and resume building tools via its MCP endpoint.
  name: ATSPrep API
  slug: atsprep-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/atsprep-com/plans/atsprep-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atsprep-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/atsprep-com/changelog/atsprep-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/atsprep-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/atsprep-com/llms/atsprep-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atsprep-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/atsprep-com/mcp/atsprep-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atsprep-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/atsprep-com/hosts/atsprep-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atsprep-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atsprep-com/vendors/atsprep-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atsprep-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://atsprep.com/ats-resume-template/registered-nurse
- group: operate
  title: ''
  type: ChangeLog
  url: https://atsprep.com/changelog
- group: auth
  href: https://artifacts.apis.io/atsprep-com/security/atsprep-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atsprep-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atsprep.com/
- group: company
  title: ''
  type: Blog
  url: https://atsprep.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://atsprep.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atsprep.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atsprep.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://atsprep.com/contact
created: '2026-11-02'
description: ATSPrep is a free, evidence‑first resume builder and job tracker that lets users tailor resumes with verifiable achievements, save multiple versions, track applications, and check PDF text recovery before submission. The web‑based tool runs locally in the browser, requires no account for core features, and offers optional paid Pro plans for AI‑enhanced editing and additional templates. It supports importing resumes from PDF, DOCX, TXT, or Markdown, provides a job‑fit matcher, and ensures privacy by never uploading personal data.
image: https://atsprep.com/icons/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at atsprep.com.
  name: ATSPrep MCP Server
  slug: atsprep-com-mcp-yml
modified: '2026-11-02'
name: ATSPrep
nav: Providers
network: true
overview: 'ATSPrep is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Resume Builder, Job-Tracker, Careers, and Applicant Tracking.


  ATSPrep''s developer surface includes changelog, signup flow, engineering blog, pricing, support, and 10 more developer resources.'
plans:
- name: Atsprep Com Plans Pricing
  plan_count: 3
  slug: atsprep-com-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.3
    operational_transparency: 7.9
  previous_composite: 24.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atsprep Com Domain Security
  slug: atsprep-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: atsprep-com
tags:
- Resume Builder
- Job-Tracker
- Careers
- Applicant Tracking
website: https://atsprep.com/
---
