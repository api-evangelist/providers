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
  - '{''url'': ''https://www.kennasecurity.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.cisco.com/site/us/en/products/security/vulnerability-management/kenna-is-part-of-cisco/index.html — a different registrable domain (kennasecurity.com -> cisco.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 33.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 45
  human_in_the_loop: 1
  name: Kenna Security Agentic Access
  operation_count: 120
  slug: kenna-security-agentic-access
  summary_line: 120 operations · 45 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: 'REST API for the Kenna / Cisco Vulnerability Management platform: manage assets, asset groups, applications, findings, fixes, vulnerabilities, vulnerability intelligence, connectors, data exports, das'
  name: Cisco Vulnerability Management API (Kenna)
  slug: cisco-vulnerability-management-api-kenna
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The APPLICATION REPORTING API from Kenna Security — 3 operation(s) for application reporting.
  name: Kenna Security APPLICATION REPORTING API
  slug: kenna-security-application-reporting-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The APPLICATIONS API from Kenna Security — 2 operation(s) for applications.
  name: Kenna Security APPLICATIONS API
  slug: kenna-security-applications-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The ASSET GROUP REPORTING API from Kenna Security — 12 operation(s) for asset group reporting.
  name: Kenna Security ASSET GROUP REPORTING API
  slug: kenna-security-asset-group-reporting-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The ASSET GROUPS API from Kenna Security — 6 operation(s) for asset groups.
  name: Kenna Security ASSET GROUPS API
  slug: kenna-security-asset-groups-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The ASSET TAGGING API from Kenna Security — 1 operation(s) for asset tagging.
  name: Kenna Security ASSET TAGGING API
  slug: kenna-security-asset-tagging-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The ASSETS API from Kenna Security — 7 operation(s) for assets.
  name: Kenna Security ASSETS API
  slug: kenna-security-assets-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The AUDIT LOGS API from Kenna Security — 1 operation(s) for audit logs.
  name: Kenna Security AUDIT LOGS API
  slug: kenna-security-audit-logs-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The CONNECTOR RUNS API from Kenna Security — 4 operation(s) for connector runs.
  name: Kenna Security CONNECTOR RUNS API
  slug: kenna-security-connector-runs-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The CONNECTORS API from Kenna Security — 2 operation(s) for connectors.
  name: Kenna Security CONNECTORS API
  slug: kenna-security-connectors-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The CVES API from Kenna Security — 1 operation(s) for cves.
  name: Kenna Security CVES API
  slug: kenna-security-cves-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The DASHBOARD GROUPS API from Kenna Security — 2 operation(s) for dashboard groups.
  name: Kenna Security DASHBOARD GROUPS API
  slug: kenna-security-dashboard-groups-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The DATA EXPORT API from Kenna Security — 3 operation(s) for data export.
  name: Kenna Security DATA EXPORT API
  slug: kenna-security-data-export-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The ENTITLEMENTS API from Kenna Security — 1 operation(s) for entitlements.
  name: Kenna Security ENTITLEMENTS API
  slug: kenna-security-entitlements-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The FINDINGS API from Kenna Security — 3 operation(s) for findings.
  name: Kenna Security FINDINGS API
  slug: kenna-security-findings-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The FIXES API from Kenna Security — 4 operation(s) for fixes.
  name: Kenna Security FIXES API
  slug: kenna-security-fixes-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The HIGH RISK VULNERABILITY DENSITIES API from Kenna Security — 1 operation(s) for high risk vulnerability densities.
  name: Kenna Security HIGH RISK VULNERABILITY DENSITIES API
  slug: kenna-security-high-risk-vulnerability-densities-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The INFERENCE V1 (Legacy) API from Kenna Security — 2 operation(s) for inference v1 (legacy).
  name: Kenna Security INFERENCE V1 (Legacy) API
  slug: kenna-security-inference-v1-legacy-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The INFERENCE V2 (Legacy) API from Kenna Security — 1 operation(s) for inference v2 (legacy).
  name: Kenna Security INFERENCE V2 (Legacy) API
  slug: kenna-security-inference-v2-legacy-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The INFERENCE V3 - Cves API from Kenna Security — 1 operation(s) for inference v3 - cves.
  name: Kenna Security INFERENCE V3 - Cves API
  slug: kenna-security-inference-v3-cves-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The INFERENCE V3 - Osquery API from Kenna Security — 1 operation(s) for inference v3 - osquery.
  name: Kenna Security INFERENCE V3 - Osquery API
  slug: kenna-security-inference-v3-osquery-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The INTEGRATIONS API from Kenna Security — 2 operation(s) for integrations.
  name: Kenna Security INTEGRATIONS API
  slug: kenna-security-integrations-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The REMEDIATION SCORE API from Kenna Security — 1 operation(s) for remediation score.
  name: Kenna Security REMEDIATION SCORE API
  slug: kenna-security-remediation-score-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The ROLES API from Kenna Security — 7 operation(s) for roles.
  name: Kenna Security ROLES API
  slug: kenna-security-roles-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The SLA ADHERENCE API from Kenna Security — 1 operation(s) for sla adherence.
  name: Kenna Security SLA ADHERENCE API
  slug: kenna-security-sla-adherence-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The STACKS API from Kenna Security — 4 operation(s) for stacks.
  name: Kenna Security STACKS API
  slug: kenna-security-stacks-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The USERS API from Kenna Security — 3 operation(s) for users.
  name: Kenna Security USERS API
  slug: kenna-security-users-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The VULNERABILITIES API from Kenna Security — 8 operation(s) for vulnerabilities.
  name: Kenna Security VULNERABILITIES API
  slug: kenna-security-vulnerabilities-api
- baseURL: https://api.kennasecurity.com
  baseurl_source: declared
  description: The VULNERABILITY INTELLIGENCE+ API from Kenna Security — 9 operation(s) for vulnerability intelligence+.
  name: Kenna Security VULNERABILITY INTELLIGENCE+ API
  slug: kenna-security-vulnerability-intelligence-api
artifact_total: 46
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/agentic-access/kenna-security-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kenna-security-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/rules/kenna-security-rules.yml
  title: ''
  type: Spectral
  url: rules/kenna-security-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/json-ld/kenna-security-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kenna-security-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/vocabulary/kenna-security-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kenna-security-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/data-model/kenna-security-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kenna-security-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/errors/kenna-security-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kenna-security-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/conformance/kenna-security-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kenna-security-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/a2a/kenna-security-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kenna-security-a2a.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/hosts/kenna-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kenna-security-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/vendors/kenna-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kenna-security-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/packages/kenna-security-packages.yml
  title: ''
  type: SDKs
  url: packages/kenna-security-packages.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: company
  title: ''
  type: Website
  url: https://www.kennasecurity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.kennasecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.kennasecurity.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.kennasecurity.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.kennasecurity.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.kennasecurity.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://learn-cloudsecurity.cisco.com/vulnerability-management-resources
- group: operate
  title: ''
  type: Support
  url: https://help.kennasecurity.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kennasecurity.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KennaSecurity
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/authentication/kenna-security-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kenna-security-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/conventions/kenna-security-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kenna-security-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/lifecycle/kenna-security-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kenna-security-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.kennasecurity.com/docs/getting-started-with-vulnerability-inference-v2
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/changelog/kenna-security-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kenna-security-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/packages/kenna-security-packages.yml
  title: ''
  type: Packages
  url: packages/kenna-security-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/cli/kenna-security-cli.yml
  title: ''
  type: CLI
  url: cli/kenna-security-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/llms/kenna-security-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kenna-security-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/security/kenna-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kenna-security-domain-security.yml
created: '2026-07-17'
description: 'Kenna Security is the risk-based vulnerability management platform now part of Cisco as Cisco Vulnerability Management. Founded in Chicago and acquired by Cisco in 2021, the platform ingests scanner, asset, and threat-intelligence data to prioritize vulnerabilities by real-world exploitability and business risk. It exposes a REST API (the Kenna / Cisco Vulnerability Management API) at api.kennasecurity.com covering assets, asset groups, applications, findings, fixes, vulnerabilities, vulnerability intelligence, connectors, data exports, dashboards, metrics, roles, and users. The API uses an X-Risk-Token API-key header over HTTPS, page-number pagination, and JSON payloads. Kenna also publishes a first-party open-source Scripting Toolkit on GitHub for building connectors and integrations. Sector: cybersecurity / vulnerability management.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kenna-security.png
json_schemas:
- name: 51612701083eea34cbeb0be66175b235566839e2376216d7ff4bab8b393d98fd_post_response_schema
  property_count: 0
  slug: kenna-security-51612701083eea34cbeb0be66175b235566839e2376216d7ff4bab8b393d98fd-post-response-schema
- name: create_vulnerability_request_body_schema
  property_count: 23
  slug: kenna-security-create-vulnerability-request-body-schema
- name: exported_finding
  property_count: 19
  slug: kenna-security-export-get-finding-response-schema
- name: exported_vulnerability
  property_count: 43
  slug: kenna-security-export-get-vulnerability-response-schema
- name: export_settings_request_body_schema
  property_count: 52
  slug: kenna-security-export-settings-request-body-schema
- name: microsoft_vuln_inferenece_post_response_schema
  property_count: 0
  slug: kenna-security-microsoft-vuln-inferenece-post-response-schema
- name: odata_cve_response_schema
  property_count: 32
  slug: kenna-security-odata-cve-response-schema
- name: os_inference_response_schema
  property_count: 6
  slug: kenna-security-os-inference-response-schema
- name: v3_os_inference_response_schema
  property_count: 8
  slug: kenna-security-v3-os-inference-response-schema
- name: vulnerability_definition_schema
  property_count: 48
  slug: kenna-security-vulnerability-definition-schema
- name: vulnerability_definition_with_mitre_attack_schema
  property_count: 49
  slug: kenna-security-vulnerability-definition-with-mitre-attack-schema
- name: windows_os_inference_request_body_schema
  property_count: 0
  slug: kenna-security-windows-os-inference-request-body-schema
jsonld:
- class_count: 116
  name: Kenna Security Context
  property_count: 349
  slug: kenna-security-context
layout: provider
modified: '2026-08-19'
name: Kenna Security
nav: Providers
network: true
overview: 'Kenna Security publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including APPLICATION REPORTING API, APPLICATIONS API, ASSET GROUP REPORTING API, and 26 more. Tagged areas include Company, Cybersecurity, Vulnerability Management, Risk-Based Prioritization, and Threat Intelligence.


  The Kenna Security catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kenna Security''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, authentication, and 24 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Kenna Security API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: kenna-security-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 64.4
    developer_ergonomics: 48.8
    discoverability: 73.2
    operational_transparency: 30.3
  previous_composite: 19.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 28
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/kenna-security/refs/heads/main/screenshots/kenna-security-2026-07-25T223615.png
security:
- kind: authentication
  name: Kenna Security Authentication
  slug: kenna-security-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kenna Security Domain Security
  slug: kenna-security-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kenna-security
tags:
- Company
- Cybersecurity
- Vulnerability Management
- Risk-Based Prioritization
- Threat Intelligence
- Security
- Cisco
- REST API
website: https://www.kennasecurity.com
---
