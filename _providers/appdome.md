---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Appdome Agentic Access
  operation_count: 53
  slug: appdome-agentic-access
  summary_line: 53 operations · 32 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The Appdome Build2Secure (DEV-API) REST API automates Appdome's no-code mobile app defense pipeline — upload, build/fuse, add context, sign (standard, private, and Auto-DEV signing), download, publish
  name: Appdome Build2Secure API
  slug: appdome-build2secure-api
- baseURL: https://fusion.appdome.com/api/v1
  baseurl_source: declared
  description: The API Account Maintenance API from Appdome — 8 operation(s) for api account maintenance.
  name: Appdome API Account Maintenance API
  slug: appdome-api-account-maintenance-api
- baseURL: https://fusion.appdome.com/api/v1
  baseurl_source: declared
  description: The API Team Management API from Appdome — 4 operation(s) for api team management.
  name: Appdome API Team Management API
  slug: appdome-api-team-management-api
- baseURL: https://fusion.appdome.com/api/v1
  baseurl_source: declared
  description: The API User Management API from Appdome — 5 operation(s) for api user management.
  name: Appdome API User Management API
  slug: appdome-api-user-management-api
- baseURL: https://fusion.appdome.com/api/v1
  baseurl_source: declared
  description: The App Validation API from Appdome — 2 operation(s) for app validation.
  name: Appdome App Validation API
  slug: appdome-app-validation-api
- baseURL: https://fusion.appdome.com/api/v1
  baseurl_source: declared
  description: The Device Match API from Appdome — 2 operation(s) for device match.
  name: Appdome Device Match API
  slug: appdome-device-match-api
- baseURL: https://fusion.appdome.com/api/v1
  baseurl_source: declared
  description: The Secure Certificate API from Appdome — 3 operation(s) for secure certificate.
  name: Appdome Secure Certificate API
  slug: appdome-secure-certificate-api
- baseURL: https://fusion.appdome.com/api/v1
  baseurl_source: declared
  description: The Tasks API from Appdome — 22 operation(s) for tasks.
  name: Appdome Tasks API
  slug: appdome-tasks-api
artifact_total: 17
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/agentic-access/appdome-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/appdome-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/rules/appdome-rules.yml
  title: ''
  type: Spectral
  url: rules/appdome-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/json-ld/appdome-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appdome-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/vocabulary/appdome-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appdome-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/hosts/appdome-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appdome-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/vendors/appdome-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appdome-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/security/appdome-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appdome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appdome.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apis.appdome.com/docs/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://apis.appdome.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://apis.appdome.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apis.appdome.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://fusion.appdome.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://fusion.appdome.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appdome.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.appdome.com/dev-sec-blog/
- group: operate
  title: ''
  type: Support
  url: https://www.appdome.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.appdome.com/how-to/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appdome.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appdome.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Appdome
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/packages/appdome-packages.yml
  title: ''
  type: Packages
  url: packages/appdome-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/packages/appdome-packages.yml
  title: ''
  type: SDKs
  url: packages/appdome-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/cli/appdome-cli.yml
  title: ''
  type: CLI
  url: cli/appdome-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/authentication/appdome-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appdome-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/llms/appdome-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appdome-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/conventions/appdome-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appdome-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/errors/appdome-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appdome-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/lifecycle/appdome-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appdome-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/data-model/appdome-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appdome-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/mcp/appdome-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/appdome-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/conformance/appdome-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appdome-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Appdome is a mobile app defense and DevSecOps platform that lets development and security teams add cyber-defense, anti-fraud, anti-malware, anti-cheat, and runtime protections to Android and iOS apps with no code and no SDK. Its Build2Secure ("DEV-API") REST API connects the no-code build, fuse, context, sign, and publish steps to CI/CD systems such as GitHub, GitLab, Jenkins, Azure DevOps, Bitrise, CircleCI, and TeamCity, enabling teams to protect, sign, certify, and release mobile apps automatically at scale. The platform also covers app validation, Certified Secure certificates, team and user management, DEV-Logs audit events, and device-matching services. Appdome is backed by Menlo Ventures.
image: https://www.appdome.com/wp-content/uploads/2025/10/cropped-AppdomeShield-270x270.png
json_schemas:
- name: CompareRequest
  property_count: 2
  slug: appdome-compare-request
- name: CompareResponse
  property_count: 3
  slug: appdome-compare-response
- name: DiscoverRequest
  property_count: 4
  slug: appdome-discover-request
- name: DiscoverResult
  property_count: 2
  slug: appdome-discover-result
jsonld:
- class_count: 5
  name: Appdome Context
  property_count: 9
  slug: appdome-context
layout: provider
modified: '2026-07-17'
name: Appdome
nav: Providers
network: true
overview: 'Appdome publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Account Maintenance API, API Team Management API, API User Management API, and 5 more. Tagged areas include Company, Mobile App Security, Mobile App Defense, DevSecOps, and Application Security.


  The Appdome catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Appdome''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 26 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Appdome API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: appdome-rules
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.8
  facets:
    access_clarity: 38.2
    contract_governance: 22.0
    contract_quality: 61.3
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/appdome/refs/heads/main/screenshots/appdome-2026-07-25T200727.png
security:
- kind: authentication
  name: Appdome Authentication
  slug: appdome-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Appdome Domain Security
  slug: appdome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appdome
tags:
- Company
- Mobile App Security
- Mobile App Defense
- DevSecOps
- Application Security
- Mobile
- CI/CD
- App Signing
- Fraud Prevention
- Code Signing
- Developer Tools
website: https://appdome.com
---
