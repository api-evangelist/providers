---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 5
apis:
- baseURL: http://cities.internal.my-company.com
  baseurl_source: declared
  description: The App API from Cortex Applications, Inc. — 2 operation(s) for app.
  name: Cortex Applications, Inc. App API
  slug: cortex-applications-inc-app-api
- baseURL: http://cities.internal.my-company.com
  baseurl_source: declared
  description: The Cities API from Cortex Applications, Inc. — 1 operation(s) for cities.
  name: Cortex Applications, Inc. Cities API
  slug: cortex-applications-inc-cities-api
- baseURL: http://cities.internal.my-company.com
  baseurl_source: declared
  description: The Meta API from Cortex Applications, Inc. — 1 operation(s) for meta.
  name: Cortex Applications, Inc. Meta API
  slug: cortex-applications-inc-meta-api
- baseURL: http://cities.internal.my-company.com
  baseurl_source: declared
  description: The Orgs API from Cortex Applications, Inc. — 2 operation(s) for orgs.
  name: Cortex Applications, Inc. Orgs API
  slug: cortex-applications-inc-orgs-api
- baseURL: http://cities.internal.my-company.com
  baseurl_source: declared
  description: The Repos API from Cortex Applications, Inc. — 4 operation(s) for repos.
  name: Cortex Applications, Inc. Repos API
  slug: cortex-applications-inc-repos-api
artifact_total: 12
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/rules/cortex-applications-inc-rules.yml
  title: ''
  type: Spectral
  url: rules/cortex-applications-inc-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/json-ld/cortex-applications-inc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cortex-applications-inc-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/vocabulary/cortex-applications-inc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cortex-applications-inc-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/data-model/cortex-applications-inc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cortex-applications-inc-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/authentication/cortex-applications-inc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cortex-applications-inc-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/conformance/cortex-applications-inc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cortex-applications-inc-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/llms/cortex-applications-inc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cortex-applications-inc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/a2a/cortex-applications-inc-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cortex-applications-inc-a2a.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/hosts/cortex-applications-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cortex-applications-inc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/vendors/cortex-applications-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cortex-applications-inc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cortex.io/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cortex.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cortex.io/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cortex.io/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.cortex.io/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cortexapps
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cortex.io/solutions/developers
- group: company
  title: ''
  type: Blog
  url: https://www.cortex.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cortex.io/guides/dev-onboarding/env-setup-workflow
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cortex.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cortex.io/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cortex-applications-inc/refs/heads/main/security/cortex-applications-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cortex-applications-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cortex.io
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cortex.io
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Cortex Applications, Inc. provides an Engineering Operations Platform that centralizes data from tooling, offers AI‑driven insights, scorecards, and golden‑path workflows to improve developer productivity, operational maturity, and reduce MTTR. The platform serves enterprises and startups, integrating with CI/CD, monitoring, and incident management tools to deliver a unified view of software delivery and AI‑augmented decision making.
image: https://a-us.storyblok.com/f/1021527/1200x642/96bbfca52d/cortex-og-meta-dora.jpg
json_schemas:
- name: GetReposOwnerRepoActionsVariablesNameResponse
  property_count: 1
  slug: cortex-applications-inc-get-repos-owner-repo-actions-variables-name-response
- name: PatchReposOwnerRepoActionsVariablesNameRequest
  property_count: 1
  slug: cortex-applications-inc-patch-repos-owner-repo-actions-variables-name-request
- name: PostReposOwnerRepoActionsVariablesRequest
  property_count: 2
  slug: cortex-applications-inc-post-repos-owner-repo-actions-variables-request
jsonld:
- class_count: 3
  name: Cortex Applications Inc Context
  property_count: 2
  slug: cortex-applications-inc-context
layout: provider
modified: '2026-10-11'
name: Cortex Applications, Inc.
nav: Providers
network: true
overview: 'Cortex Applications, Inc. is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including App API, Cities API, Meta API, and 2 more. Tagged areas include Company, Engineering, Platform, Artificial Intelligence, and Developer Productivity.


  The Cortex Applications, Inc. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cortex Applications, Inc.''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 17 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Cortex Applications, Inc. API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: cortex-applications-inc-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 21.4
    developer_ergonomics: 52.4
    discoverability: 80.4
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cortex Applications Inc Authentication
  slug: cortex-applications-inc-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cortex Applications Inc Domain Security
  slug: cortex-applications-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cortex-applications-inc
tags:
- Company
- Engineering
- Platform
- Artificial Intelligence
- Developer Productivity
website: https://www.cortex.io
---
