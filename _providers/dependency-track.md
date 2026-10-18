---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 137
  human_in_the_loop: 1
  name: Dependency Track Agentic Access
  operation_count: 272
  slug: dependency-track-agentic-access
  summary_line: 272 operations · 137 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Protocol Buffers (proto3, package org.dependencytrack.notification.v1) message definitions for Dependency-Track notification payloads, published in the DependencyTrack/docs repository. The file define
  name: Dependency-Track Notifications
  slug: dependency-track-notifications
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The acl API from Dependency-Track — 3 operation(s) for acl.
  name: Dependency-Track Acl API
  slug: dependency-track-acl-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The analysis API from Dependency-Track — 1 operation(s) for analysis.
  name: Dependency-Track Analysis API
  slug: dependency-track-analysis-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The badge API from Dependency-Track — 4 operation(s) for badge.
  name: Dependency-Track Badge API
  slug: dependency-track-badge-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The bom API from Dependency-Track — 4 operation(s) for bom.
  name: Dependency-Track Bom API
  slug: dependency-track-bom-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The calculator API from Dependency-Track — 2 operation(s) for calculator.
  name: Dependency-Track Calculator API
  slug: dependency-track-calculator-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The component API from Dependency-Track — 8 operation(s) for component.
  name: Dependency-Track Component API
  slug: dependency-track-component-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The componentProperty API from Dependency-Track — 2 operation(s) for componentproperty.
  name: Dependency-Track Component Property API
  slug: dependency-track-componentproperty-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to components
  name: Dependency-Track Components API
  slug: dependency-track-components-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The configProperty API from Dependency-Track — 4 operation(s) for configproperty.
  name: Dependency-Track Config Property API
  slug: dependency-track-configproperty-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The cwe API from Dependency-Track — 2 operation(s) for cwe.
  name: Dependency-Track Cwe API
  slug: dependency-track-cwe-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The dependencyGraph API from Dependency-Track — 2 operation(s) for dependencygraph.
  name: Dependency-Track Dependency Graph API
  slug: dependency-track-dependencygraph-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The event API from Dependency-Track — 1 operation(s) for event.
  name: Dependency-Track Event API
  slug: dependency-track-event-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to extensions
  name: Dependency-Track Extensions API
  slug: dependency-track-extensions-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The finding API from Dependency-Track — 5 operation(s) for finding.
  name: Dependency-Track Finding API
  slug: dependency-track-finding-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to KEV data sources
  name: Dependency-Track Kev Data Sources API
  slug: dependency-track-kev-data-sources-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The ldap API from Dependency-Track — 4 operation(s) for ldap.
  name: Dependency-Track Ldap API
  slug: dependency-track-ldap-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The license API from Dependency-Track — 3 operation(s) for license.
  name: Dependency-Track License API
  slug: dependency-track-license-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The licenseGroup API from Dependency-Track — 3 operation(s) for licensegroup.
  name: Dependency-Track License Group API
  slug: dependency-track-licensegroup-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The metrics API from Dependency-Track — 13 operation(s) for metrics.
  name: Dependency-Track Metrics API
  slug: dependency-track-metrics-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The notification API from Dependency-Track — 8 operation(s) for notification.
  name: Dependency-Track Notification API
  slug: dependency-track-notification-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to OAuth 2.0 token issuance
  name: Dependency-Track OAuth API
  slug: dependency-track-oauth-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The oidc API from Dependency-Track — 7 operation(s) for oidc.
  name: Dependency-Track Oidc API
  slug: dependency-track-oidc-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The permission API from Dependency-Track — 5 operation(s) for permission.
  name: Dependency-Track Permission API
  slug: dependency-track-permission-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The policy API from Dependency-Track — 3 operation(s) for policy.
  name: Dependency-Track Policy API
  slug: dependency-track-policy-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The policyCondition API from Dependency-Track — 3 operation(s) for policycondition.
  name: Dependency-Track Policy Condition API
  slug: dependency-track-policycondition-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The project API from Dependency-Track — 14 operation(s) for project.
  name: Dependency-Track Project API
  slug: dependency-track-project-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The projectProperty API from Dependency-Track — 1 operation(s) for projectproperty.
  name: Dependency-Track Project Property API
  slug: dependency-track-projectproperty-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to projects
  name: Dependency-Track Projects API
  slug: dependency-track-projects-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The repository API from Dependency-Track — 4 operation(s) for repository.
  name: Dependency-Track Repository API
  slug: dependency-track-repository-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to secrets
  name: Dependency-Track Secrets API
  slug: dependency-track-secrets-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to service accounts
  name: Dependency-Track Service Accounts API
  slug: dependency-track-service-accounts-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The service API from Dependency-Track — 3 operation(s) for service.
  name: Dependency-Track Service API
  slug: dependency-track-service-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints exposing the capabilities of the running server
  name: Dependency-Track System Capabilities API
  slug: dependency-track-system-capabilities-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The tag API from Dependency-Track — 7 operation(s) for tag.
  name: Dependency-Track Tag API
  slug: dependency-track-tag-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to task queue management
  name: Dependency-Track Task Queues API
  slug: dependency-track-task-queues-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The team API from Dependency-Track — 7 operation(s) for team.
  name: Dependency-Track Team API
  slug: dependency-track-team-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The user API from Dependency-Track — 11 operation(s) for user.
  name: Dependency-Track User API
  slug: dependency-track-user-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The version API from Dependency-Track — 1 operation(s) for version.
  name: Dependency-Track Version API
  slug: dependency-track-version-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The vex API from Dependency-Track — 2 operation(s) for vex.
  name: Dependency-Track Vex API
  slug: dependency-track-vex-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The violation API from Dependency-Track — 3 operation(s) for violation.
  name: Dependency-Track Violation API
  slug: dependency-track-violation-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The violationanalysis API from Dependency-Track — 1 operation(s) for violationanalysis.
  name: Dependency-Track Violationanalysis API
  slug: dependency-track-violationanalysis-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to vulnerability data sources
  name: Dependency-Track Vuln Data Sources API
  slug: dependency-track-vuln-data-sources-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to vulnerability policies
  name: Dependency-Track Vuln Policies API
  slug: dependency-track-vuln-policies-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: The vulnerability API from Dependency-Track — 11 operation(s) for vulnerability.
  name: Dependency-Track Vulnerability API
  slug: dependency-track-vulnerability-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to vulnerabilities
  name: Dependency-Track Vulns API
  slug: dependency-track-vulns-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to workflows
  name: Dependency-Track Workflows API
  slug: dependency-track-workflows-api
- baseURL: http://{hostname}:{port}/api
  baseurl_source: declared
  description: Endpoints related to workload identity providers
  name: Dependency-Track Workload Identity Providers API
  slug: dependency-track-workload-identity-providers-api
artifact_total: 68
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/agentic-access/dependency-track-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dependency-track-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/plans/dependency-track-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dependency-track-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/rules/dependency-track-rules.yml
  title: ''
  type: Spectral
  url: rules/dependency-track-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/rules/dependency-track-dependency-track-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/dependency-track-dependency-track-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/json-ld/dependency-track-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dependency-track-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/vocabulary/dependency-track-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dependency-track-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/data-model/dependency-track-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dependency-track-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/conventions/dependency-track-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dependency-track-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/lifecycle/dependency-track-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/dependency-track-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/lifecycle/dependency-track-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dependency-track-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/errors/dependency-track-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dependency-track-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/conformance/dependency-track-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dependency-track-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/overlays/dependency-track-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dependency-track-v1-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/well-known/dependency-track-owasp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dependency-track-owasp-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/well-known/dependency-track-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dependency-track-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/hosts/dependency-track-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dependency-track-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/vendors/dependency-track-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dependency-track-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/packages/dependency-track-packages.yml
  title: ''
  type: SDKs
  url: packages/dependency-track-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/packages/dependency-track-packages.yml
  title: ''
  type: Packages
  url: packages/dependency-track-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/authentication/dependency-track-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dependency-track-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/security/dependency-track-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dependency-track-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dependencytrack.org/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/DependencyTrack/dependency-track/blob/e3abb0a09bb4dd7a8e926a26eda6c1b6324fd76c/api/src/main/spectral/ruleset.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dependencytrack.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dependencytrack.org/integrations/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dependencytrack.org/getting-started/distributions/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dependencytrack.org/changelog/
- group: company
  title: ''
  type: Blog
  url: https://dependencytrack.org/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DependencyTrack
- group: operate
  title: ''
  type: Support
  url: https://github.com/DependencyTrack/dependency-track/discussions
- group: operate
  title: ''
  type: Releases
  url: https://github.com/DependencyTrack/dependency-track/releases
- group: other
  title: ''
  type: Download
  url: https://dependencytrack.org/download
- group: other
  title: ''
  type: ProjectPage
  url: https://owasp.org/www-project-dependency-track/
- group: other
  title: ''
  type: DockerHub
  url: https://hub.docker.com/u/dependencytrack/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@DependencyTrack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/owasp-dependency-track
created: '2026-10-09'
description: Dependency-Track is an OWASP flagship open source Component Analysis platform for Software Bill of Materials (SBOM) analysis. Per its site, over 20,000 organizations use it to inventory components, find vulnerabilities, and enforce policy across the software supply chain. It is self-hosted (distributed as Docker images) and exposes a REST API, documented with OpenAPI/Swagger, on each deployed instance at /api.
image: https://dependencytrack.org/assets/images/social-card-og.png
json_schemas:
- name: clone-project-request
  property_count: 3
  slug: dependency-track-clone-project-request
- name: Component
  property_count: 51
  slug: dependency-track-component
- name: create-component-request
  property_count: 21
  slug: dependency-track-create-component-request
- name: create-oauth-token-request
  property_count: 6
  slug: dependency-track-create-oauth-token-request
- name: create-workload-identity-provider-request
  property_count: 7
  slug: dependency-track-create-workload-identity-provider-request
- name: NotificationRule
  property_count: 20
  slug: dependency-track-notification-rule
- name: PortfolioMetrics
  property_count: 33
  slug: dependency-track-portfolio-metrics
- name: ProjectMetrics
  property_count: 31
  slug: dependency-track-project-metrics
- name: Project
  property_count: 33
  slug: dependency-track-project
- name: update-workload-identity-provider-request
  property_count: 5
  slug: dependency-track-update-workload-identity-provider-request
- name: Vulnerability
  property_count: 45
  slug: dependency-track-vulnerability
- name: workload-identity-provider
  property_count: 8
  slug: dependency-track-workload-identity-provider
jsonld:
- class_count: 120
  name: Dependency Track Context
  property_count: 339
  slug: dependency-track-context
layout: provider
modified: '2026-10-09'
name: Dependency-Track
nav: Providers
network: true
overview: 'Dependency-Track publishes 48 API contracts indexed on the [APIs.io](https://apis.io/) network, including Acl API, Analysis API, Badge API, and 45 more. Tagged areas include Company, SBOM, Software Supply Chain, Vulnerability Management, and Open Source.


  The Dependency-Track catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dependency-Track''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, engineering blog, support, and 30 more developer resources.'
plans:
- name: Dependency Track Plans Pricing
  plan_count: 1
  slug: dependency-track-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Dependency Track Rate Limits
  slug: dependency-track-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 54
  extends:
  - spectral:oas
  - ./zalando.yaml
  name: Dependency-Track — dependency track rules
  rule_count: 13
  severity_counts:
    error: 13
    hint: 0
    info: 0
    warn: 0
  slug: dependency-track-dependency-track-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Dependency-Track API Rules
  rule_count: 16
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 7
  slug: dependency-track-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 64.8
    developer_ergonomics: 56.5
    discoverability: 62.5
    operational_transparency: 28.9
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 47
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/dependency-track/refs/heads/main/screenshots/dependency-track-2026-10-11T103651.png
security:
- kind: authentication
  name: Dependency Track Authentication
  slug: dependency-track-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dependency Track Domain Security
  slug: dependency-track-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dependency-track
tags:
- Company
- SBOM
- Software Supply Chain
- Vulnerability Management
- Open Source
- OWASP
- Security
- CycloneDX
website: https://dependencytrack.org/
---
