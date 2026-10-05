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
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-10-04'
api_count: 6
apis:
- description: REST API for Black Duck SCA (Hub) — projects, versions, components, vulnerabilities, policies, scans, and reports. Each Black Duck server publishes its own OpenAPI 3 document at /api-doc/openapi3-publ
  name: Black Duck SCA REST API
  slug: black-duck-sca-rest-api
- baseURL: https://polaris.blackduck.com
  baseurl_source: declared
  description: The Black Duck API API from Black Duck — 1 operation(s) for black duck api.
  name: Black Duck Black Duck API
  slug: black-duck-black-duck-api-api
- baseURL: https://polaris.blackduck.com
  baseurl_source: declared
  description: The Issues API from Black Duck — 1 operation(s) for issues.
  name: Black Duck Issues API
  slug: black-duck-issues-api
- baseURL: https://polaris.blackduck.com
  baseurl_source: declared
  description: The Projects API from Black Duck — 3 operation(s) for projects.
  name: Black Duck Projects API
  slug: black-duck-projects-api
- baseURL: https://polaris.blackduck.com
  baseurl_source: declared
  description: The Search API from Black Duck — 1 operation(s) for search.
  name: Black Duck Search API
  slug: black-duck-search-api
- baseURL: https://polaris.blackduck.com
  baseurl_source: declared
  description: The Users API from Black Duck — 1 operation(s) for users.
  name: Black Duck Users API
  slug: black-duck-users-api
artifact_total: 15
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackduck.com/company/legal/privacy-policy.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/rules/black-duck-rules.yml
  title: ''
  type: Spectral
  url: rules/black-duck-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/json-ld/black-duck-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/black-duck-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/vocabulary/black-duck-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/black-duck-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/data-model/black-duck-data-model.yml
  title: ''
  type: DataModel
  url: data-model/black-duck-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/conformance/black-duck-conformance.yml
  title: ''
  type: Conformance
  url: conformance/black-duck-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/mcp/black-duck-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/black-duck-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/hosts/black-duck-hosts.yml
  title: ''
  type: Hosts
  url: hosts/black-duck-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/vendors/black-duck-vendors.yml
  title: ''
  type: Vendors
  url: vendors/black-duck-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://www.blackduck.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/security/black-duck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/black-duck-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.blackduck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.blackduck.com/category/api
- group: docs
  title: ''
  type: APIReference
  url: https://community.blackduck.com/s/article/Blackduck-API-documentation-swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://community.blackduck.com/s/article/Black-Duck-HUB-How-to-view-the-API-documentation
- group: operate
  title: ''
  type: Support
  url: https://community.blackduck.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.blackduck.com/blog.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blackducksoftware
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blackduck.com/software-composition-analysis-tools/black-duck-sca/get-pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://www.blackduck.com/software-composition-analysis-tools/black-duck-sca/get-pricing.html
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/packages/black-duck-packages.yml
  title: ''
  type: Packages
  url: packages/black-duck-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/packages/black-duck-packages.yml
  title: ''
  type: SDKs
  url: packages/black-duck-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/cli/black-duck-cli.yml
  title: ''
  type: CLI
  url: cli/black-duck-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/mcp/black-duck-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/black-duck-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/authentication/black-duck-authentication.yml
  title: ''
  type: Authentication
  url: authentication/black-duck-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/lifecycle/black-duck-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/black-duck-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://community.blackduck.com/s/black-duck-status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/changelog/black-duck-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/black-duck-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/security/black-duck-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/black-duck-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.blackduck.com/company/legal/security-commitments.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/security/black-duck-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/black-duck-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.blackduck.com/company/legal/security-commitments.html
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI or other machine-readable contract found despite API documentation at https://documentation.blackduck.com/category/api.
  evidence:
  - status: 0
    url: https://api.blackduck.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Black Duck Software (formerly the Synopsys Software Integrity Group) is an application security company whose platform spans software composition analysis (SCA), static application security testing (SAST), dynamic application security testing (DAST), interactive application security testing (IAST), and open-source license and vulnerability management. Its API-first products — Black Duck SCA (Hub), Polaris, Coverity, and Seeker — expose REST APIs, webhooks, native CI/CD plug-ins, and the Detect command-line scanner so teams can automate open-source discovery, policy enforcement, and risk remediation across build pipelines such as Jenkins, GitHub Actions, GitLab CI, and Azure DevOps. Each Black Duck server publishes its own OpenAPI 3 document and Postman collection at /api-doc, and first-party Python and Go client libraries plus the Detect CLI wrap the API surface. This profile was seeded as a general-catalyst portfolio lead and enriched by the API Evangelist pipeline.
image: https://www.blackduck.com/content/dam/black-duck/style-guide/header/BlackDuckLogo.svg
json_schemas:
- name: GetApiV2IssuesSourcecodeinfoResponse
  property_count: 25
  slug: black-duck-get-api-v2-issues-sourcecodeinfo-response
- name: PutApiProjectsProjectidVersionsProjectversionidComponentsCom
  property_count: 1
  slug: black-duck-put-api-projects-projectid-versions-projectversionid-components-com
- name: PutApiProjects19A61354Doc25D408374Ba71F3Dd6983VersionsAbqwe3
  property_count: 1
  slug: black-duck-put-api-projects19-a61354-doc25-d408374-ba71-f3-dd6983-versions-abqwe3
jsonld:
- class_count: 3
  name: Black Duck Context
  property_count: 4
  slug: black-duck-context
layout: provider
modified: '2026-07-18'
name: Black Duck
nav: Providers
network: true
overview: 'Black Duck publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Black Duck API, Issues API, Projects API, and 3 more. Tagged areas include Company, Enterprise, Application Security, Software Composition Analysis, and SAST.


  The Black Duck catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Black Duck''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 9
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Black Duck API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: black-duck-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.5
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 21.6
    developer_ergonomics: 61.9
    discoverability: 80.0
    operational_transparency: 44.7
  previous_composite: 33.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: third-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/black-duck/refs/heads/main/screenshots/black-duck-2026-07-25T203232.png
security:
- kind: authentication
  name: Black Duck Authentication
  slug: black-duck-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Black Duck Domain Security
  slug: black-duck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Black Duck Vulnerability Disclosure
  slug: black-duck-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Black Duck Trust Center
  slug: black-duck-trust-center
  summary_line: SOC 2 Type 2, SOC 3 Type 2, ISO 27001, ISO 27017, ISO 26262, CSA STAR Self-Assessment, TISAX (Assessment Level 2), TX-RAMP Level 2
slug: black-duck
tags:
- Company
- Enterprise
- Application Security
- Software Composition Analysis
- SAST
- DAST
- Open Source Security
- DevSecOps
- Vulnerability Management
website: https://www.blackduck.com/
---
