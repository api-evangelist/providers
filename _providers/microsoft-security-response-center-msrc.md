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
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Microsoft Security Response Center Msrc Agentic Access
  operation_count: 52
  slug: microsoft-security-response-center-msrc-agentic-access
  summary_line: 52 operations
api_count: 4
apis:
- description: Report security incidents (brute force, denial of service, phishing, spam, malware) against Microsoft online services; reportable incident types are documented on the developer page.
  name: MSRC Report Abuse API
  slug: microsoft-security-response-center-msrc
- baseURL: https://api.msrc.microsoft.com/sug/v2.0
  baseurl_source: declared
  description: The Acknowledgement API from Microsoft Security Response Center (MSRC) — 4 operation(s) for acknowledgement.
  name: Microsoft Security Response Center (MSRC) Acknowledgement API
  slug: microsoft-security-response-center-msrc-acknowledgement-api
- baseURL: https://api.msrc.microsoft.com/sug/v2.0
  baseurl_source: declared
  description: The Advisory API from Microsoft Security Response Center (MSRC) — 4 operation(s) for advisory.
  name: Microsoft Security Response Center (MSRC) Advisory API
  slug: microsoft-security-response-center-msrc-advisory-api
- baseURL: https://api.msrc.microsoft.com/sug/v2.0
  baseurl_source: declared
  description: The AffectedProduct API from Microsoft Security Response Center (MSRC) — 4 operation(s) for affectedproduct.
  name: Microsoft Security Response Center (MSRC) Affected Product API
  slug: microsoft-security-response-center-msrc-affectedproduct-api
- baseURL: https://api.msrc.microsoft.com/cvrf/v3.0
  baseurl_source: declared
  description: The Csaf API from Microsoft Security Response Center (MSRC) — 1 operation(s) for csaf.
  name: Microsoft Security Response Center (MSRC) Csaf API
  slug: microsoft-security-response-center-msrc-csaf-api
- baseURL: https://api.msrc.microsoft.com/cvrf/v3.0
  baseurl_source: declared
  description: The Cvrf API from Microsoft Security Response Center (MSRC) — 2 operation(s) for cvrf.
  name: Microsoft Security Response Center (MSRC) Cvrf API
  slug: microsoft-security-response-center-msrc-cvrf-api
- baseURL: https://api.msrc.microsoft.com/sug/v2.0
  baseurl_source: declared
  description: The Deployment API from Microsoft Security Response Center (MSRC) — 4 operation(s) for deployment.
  name: Microsoft Security Response Center (MSRC) Deployment API
  slug: microsoft-security-response-center-msrc-deployment-api
- baseURL: https://api.msrc.microsoft.com/sug/v2.0
  baseurl_source: declared
  description: The HeaderContent API from Microsoft Security Response Center (MSRC) — 4 operation(s) for headercontent.
  name: Microsoft Security Response Center (MSRC) Header Content API
  slug: microsoft-security-response-center-msrc-headercontent-api
- baseURL: https://api.msrc.microsoft.com/cvrf/v3.0
  baseurl_source: declared
  description: The Metadata API from Microsoft Security Response Center (MSRC) — 10 operation(s) for metadata.
  name: Microsoft Security Response Center (MSRC) Metadata API
  slug: microsoft-security-response-center-msrc-metadata-api
- baseURL: https://api.msrc.microsoft.com/sug/v2.0
  baseurl_source: declared
  description: The ReleaseNote API from Microsoft Security Response Center (MSRC) — 4 operation(s) for releasenote.
  name: Microsoft Security Response Center (MSRC) Release Note API
  slug: microsoft-security-response-center-msrc-releasenote-api
- baseURL: https://api.msrc.microsoft.com/sug/v2.0
  baseurl_source: declared
  description: The RevisionNote API from Microsoft Security Response Center (MSRC) — 4 operation(s) for revisionnote.
  name: Microsoft Security Response Center (MSRC) Revision Note API
  slug: microsoft-security-response-center-msrc-revisionnote-api
- baseURL: https://api.msrc.microsoft.com/cvrf/v3.0
  baseurl_source: declared
  description: The Updates API from Microsoft Security Response Center (MSRC) — 7 operation(s) for updates.
  name: Microsoft Security Response Center (MSRC) Updates API
  slug: microsoft-security-response-center-msrc-updates-api
- baseURL: https://api.msrc.microsoft.com/sug/v2.0
  baseurl_source: declared
  description: The Vulnerability API from Microsoft Security Response Center (MSRC) — 4 operation(s) for vulnerability.
  name: Microsoft Security Response Center (MSRC) Vulnerability API
  slug: microsoft-security-response-center-msrc-vulnerability-api
artifact_total: 21
common:
- group: auth
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/well-known/microsoft-security-response-center-msrc-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-security-response-center-msrc-www-security.txt
- group: other
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/vendors/microsoft-security-response-center-msrc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-security-response-center-msrc-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/community
- group: agent
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/agentic-access/microsoft-security-response-center-msrc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-security-response-center-msrc-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/rules/microsoft-security-response-center-msrc-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-security-response-center-msrc-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/json-ld/microsoft-security-response-center-msrc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-security-response-center-msrc-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/vocabulary/microsoft-security-response-center-msrc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-security-response-center-msrc-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/data-model/microsoft-security-response-center-msrc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-security-response-center-msrc-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/conventions/microsoft-security-response-center-msrc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-security-response-center-msrc-conventions.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/authentication/microsoft-security-response-center-msrc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-security-response-center-msrc-authentication.yml
- group: design
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/conformance/microsoft-security-response-center-msrc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-security-response-center-msrc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/llms/microsoft-security-response-center-msrc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-security-response-center-msrc-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/well-known/microsoft-security-response-center-msrc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-security-response-center-msrc-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/well-known/microsoft-security-response-center-msrc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-security-response-center-msrc-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/hosts/microsoft-security-response-center-msrc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-security-response-center-msrc-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/packages/microsoft-security-response-center-msrc-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-security-response-center-msrc-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/packages/microsoft-security-response-center-msrc-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-security-response-center-msrc-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.microsoft.com/privacy?icid=DSM_Footer_Company_Privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/azuredevcommunityblog
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.microsoft.com/
- group: auth
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/security/microsoft-security-response-center-msrc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-security-response-center-msrc-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-security-response-center-msrc/security/microsoft-security-response-center-msrc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-security-response-center-msrc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://msrc.microsoft.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/MSRC-Microsoft-Security-Updates-API
- group: start
  title: ''
  type: DeveloperPortal
  url: https://msrc.microsoft.com/report/developer
created: '2026-05-28'
description: The Microsoft Security Response Center (MSRC) investigates vulnerabilities in Microsoft products and publishes security updates. It offers a public, anonymous, read-only CVRF API (v3.0) that serves monthly security update documents in CVRF and CSAF form, a Security Update Guide API (v2.0) exposing advisories, affected products, deployments and acknowledgements over OData, and a Report Abuse API for reporting security incidents against Microsoft online services.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-security-response-center-msrc.png
json_schemas:
- name: IEdmModel
  property_count: 6
  slug: microsoft-security-response-center-msrc-iedm-model
- name: ODataServiceDocument
  property_count: 4
  slug: microsoft-security-response-center-msrc-odata-service-document
jsonld:
- class_count: 120
  name: Microsoft Security Response Center Msrc Context
  property_count: 355
  slug: microsoft-security-response-center-msrc-context
layout: provider
modified: '2026-11-05'
name: Microsoft Security Response Center (MSRC)
nav: Providers
network: true
overview: 'Microsoft Security Response Center (MSRC) publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Acknowledgement API, Advisory API, Affected Product API, and 10 more. Tagged areas include CSAF, CVRF, OData, Public APIs, and Security.


  The Microsoft Security Response Center (MSRC) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Security Response Center (MSRC)''s developer surface includes authentication, support, changelog, engineering blog, getting-started guide, documentation, and 24 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: Microsoft Security Response Center (MSRC) API Rules
  rule_count: 29
  severity_counts:
    error: 25
    hint: 0
    info: 3
    warn: 1
  slug: microsoft-security-response-center-msrc-rules
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 36.4
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 53.1
    developer_ergonomics: 57.1
    discoverability: 69.6
    operational_transparency: 31.6
  previous_composite: 7.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/microsoft-security-response-center-msrc/microsoft-security-response-center-msrc-2026-06-20T185530.png
security:
- kind: authentication
  name: Microsoft Security Response Center Msrc Authentication
  slug: microsoft-security-response-center-msrc-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Microsoft Security Response Center Msrc Domain Security
  slug: microsoft-security-response-center-msrc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Security Response Center Msrc Vulnerability Disclosure
  slug: microsoft-security-response-center-msrc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-security-response-center-msrc
tags:
- CSAF
- CVRF
- OData
- Public APIs
- Security
- Security Updates
- Vulnerabilities
website: https://msrc.microsoft.com/
---
