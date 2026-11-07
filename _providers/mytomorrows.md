---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Mytomorrows Agentic Access
  operation_count: 42
  slug: mytomorrows-agentic-access
  summary_line: 42 operations · 31 acting
api_count: 1
apis:
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Legacy GraphQL Proxy API from myTomorrows — 1 operation(s) for legacy graphql proxy.
  name: myTomorrows Legacy GraphQL Proxy API
  slug: mytomorrows-legacy-graphql-proxy-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Public API from myTomorrows — 1 operation(s) for public.
  name: myTomorrows Public API
  slug: mytomorrows-public-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The System API from myTomorrows — 2 operation(s) for system.
  name: myTomorrows System API
  slug: mytomorrows-system-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Anno API from myTomorrows — 2 operation(s) for anno.
  name: myTomorrows Anno API
  slug: mytomorrows-anno-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Autocomplete API from myTomorrows — 1 operation(s) for autocomplete.
  name: myTomorrows Autocomplete API
  slug: mytomorrows-autocomplete-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Docs API from myTomorrows — 1 operation(s) for docs.
  name: myTomorrows Docs API
  slug: mytomorrows-docs-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Document API from myTomorrows — 1 operation(s) for document.
  name: myTomorrows Document API
  slug: mytomorrows-document-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Es API from myTomorrows — 19 operation(s) for es.
  name: myTomorrows Es API
  slug: mytomorrows-es-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Llm API from myTomorrows — 8 operation(s) for llm.
  name: myTomorrows Llm API
  slug: mytomorrows-llm-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Mdt API from myTomorrows — 1 operation(s) for mdt.
  name: myTomorrows Mdt API
  slug: mytomorrows-mdt-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Search API from myTomorrows — 3 operation(s) for search.
  name: myTomorrows Search API
  slug: mytomorrows-search-api
- baseURL: https://enterprise-search.mytomorrows.com
  baseurl_source: declared
  description: The Wrapper API from myTomorrows — 2 operation(s) for wrapper.
  name: myTomorrows Wrapper API
  slug: mytomorrows-wrapper-api
artifact_total: 21
collections:
- collection_type: open
  name: Enterprise Search Legacy GraphQL Proxy API
  slug: open-mytomorrows-legacy-graphql-proxy-api
- collection_type: open
  name: Enterprise Search Legacy GraphQL Proxy Public API
  slug: open-mytomorrows-public-api
- collection_type: open
  name: Enterprise Search Legacy GraphQL Proxy System API
  slug: open-mytomorrows-system-api
- collection_type: open
  name: Enterprise Search Legacy GraphQL Proxy V1 API
  slug: open-mytomorrows-v1-api
common:
- group: other
  href: https://artifacts.apis.io/mytomorrows/overlays/mytomorrows-enterprise-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mytomorrows-enterprise-search-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://mytomorrows.com/en/
- group: company
  title: ''
  type: Blog
  url: https://mytomorrows.com/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mytomorrows.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mytomorrows.com/en/privacy-statement
- group: auth
  href: https://artifacts.apis.io/mytomorrows/security/mytomorrows-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mytomorrows-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mytomorrows.com/
- group: agent
  href: https://artifacts.apis.io/mytomorrows/agentic-access/mytomorrows-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mytomorrows-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mytomorrows/security/mytomorrows-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mytomorrows-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/mytomorrows/mcp/mytomorrows-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mytomorrows-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mytomorrows/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mytomorrows/errors/mytomorrows-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mytomorrows-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mytomorrows/conventions/mytomorrows-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mytomorrows-conventions.yml
- group: design
  href: https://artifacts.apis.io/mytomorrows/conformance/mytomorrows-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mytomorrows-conformance.yml
- group: design
  href: https://artifacts.apis.io/mytomorrows/lifecycle/mytomorrows-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mytomorrows-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/mytomorrows/well-known/mytomorrows-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mytomorrows-well-known.yml
- group: agent
  href: https://artifacts.apis.io/mytomorrows/llms/mytomorrows-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mytomorrows-llms.txt
- group: build
  href: https://artifacts.apis.io/mytomorrows/packages/mytomorrows-packages.yml
  title: ''
  type: Packages
  url: packages/mytomorrows-packages.yml
- group: build
  href: https://artifacts.apis.io/mytomorrows/packages/mytomorrows-packages.yml
  title: ''
  type: SDKs
  url: packages/mytomorrows-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myTomorrows
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mytomorrows.com/enterprise/api-beta-program/
- group: start
  title: ''
  type: SignUp
  url: https://mytomorrows.com/enterprise/api-beta-program/
created: '2026-07-17'
description: myTomorrows is a healthcare technology platform that helps patients and healthcare professionals discover and access clinical trials and expanded-access (pre-approval) treatment options, and helps biopharma companies run and manage expanded-access programs (EAPs), collect real-world data, and recruit trial patients. Founded in 2012 by Dr. Ronald Brus, the company operates in roughly 50 countries. Its Trial Search AI product is backed by a FastAPI "Enterprise Search API" that generates Trial Search Reports (TSR), resolves conditions, and searches studies. This profile was surfaced as a portfolio company of Balderton Capital and enriched by the API Evangelist pipeline from a harvested OpenAPI and public trust surface.
image: https://mytomorrows.com/favicon.png
layout: provider
modified: '2026-07-20'
name: myTomorrows
nav: Providers
network: true
overview: 'myTomorrows publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Legacy GraphQL Proxy API, Public API, System API, and 9 more. Tagged areas include Company, Healthcare, Clinical Trials, Expanded Access, and Pharmaceuticals.


  The myTomorrows catalog on APIs.io includes 1 Spectral governance ruleset.


  myTomorrows'' developer surface includes engineering blog, signup flow, and 20 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: myTomorrows API Rules
  rule_count: 40
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 5
  slug: mytomorrows-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 40.2
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mytomorrows/mytomorrows-2026-08-07T184546.png
security:
- kind: domain-security
  name: Mytomorrows Domain Security
  slug: mytomorrows-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mytomorrows Trust Center
  slug: mytomorrows-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
skill_count: 1
skills:
- name: Generate a Trial Search Report (TSR)
  slug: mytomorrows-generate-trial-search-report
slug: mytomorrows
tags:
- Company
- Healthcare
- Clinical Trials
- Expanded Access
- Pharmaceuticals
- Patient Access
- Life Sciences
- Search
- Artificial Intelligence
website: https://mytomorrows.com/en/
---
