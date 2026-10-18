---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 85
  human_in_the_loop: 0
  name: Broad Institute Agentic Access
  operation_count: 173
  slug: broad-institute-agentic-access
  summary_line: 173 operations · 85 acting
api_count: 1
apis:
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The BillingV2 API from Broad Institute — 6 operation(s) for billingv2.
  name: Broad Institute Billing V2 API
  slug: broad-institute-billingv2-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The CromIAM Engine (for Job Manager) API from Broad Institute — 2 operation(s) for cromiam engine (for job manager).
  name: Broad Institute CromIAM Engine (for Job Manager) API
  slug: broad-institute-cromiam-engine-for-job-manager-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The CromIAM Workflows (for Admin) API from Broad Institute — 2 operation(s) for cromiam workflows (for admin).
  name: Broad Institute CromIAM Workflows (for Admin) API
  slug: broad-institute-cromiam-workflows-for-admin-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The CromIAM Workflows (for Job Manager) API from Broad Institute — 5 operation(s) for cromiam workflows (for job manager).
  name: Broad Institute CromIAM Workflows (for Job Manager) API
  slug: broad-institute-cromiam-workflows-for-job-manager-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Entities API from Broad Institute — 20 operation(s) for entities.
  name: Broad Institute Entities API
  slug: broad-institute-entities-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The GA4GH Tool Registry API from Broad Institute — 7 operation(s) for ga4gh tool registry.
  name: Broad Institute GA4GH Tool Registry API
  slug: broad-institute-ga4gh-tool-registry-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Groups API from Broad Institute — 4 operation(s) for groups.
  name: Broad Institute Groups API
  slug: broad-institute-groups-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Method Configurations API from Broad Institute — 8 operation(s) for method configurations.
  name: Broad Institute Method Configurations API
  slug: broad-institute-method-configurations-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Method Repository API from Broad Institute — 16 operation(s) for method repository.
  name: Broad Institute Method Repository API
  slug: broad-institute-method-repository-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The NIH API from Broad Institute — 3 operation(s) for nih.
  name: Broad Institute NIH API
  slug: broad-institute-nih-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Notifications API from Broad Institute — 2 operation(s) for notifications.
  name: Broad Institute Notifications API
  slug: broad-institute-notifications-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The OAuth API from Broad Institute — 2 operation(s) for oauth.
  name: Broad Institute OAuth API
  slug: broad-institute-oauth-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Profile API from Broad Institute — 8 operation(s) for profile.
  name: Broad Institute Profile API
  slug: broad-institute-profile-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Service Perimeters API from Broad Institute — 1 operation(s) for service perimeters.
  name: Broad Institute Service Perimeters API
  slug: broad-institute-service-perimeters-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Static Notebooks API from Broad Institute — 1 operation(s) for static notebooks.
  name: Broad Institute Static Notebooks API
  slug: broad-institute-static-notebooks-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Status API from Broad Institute — 3 operation(s) for status.
  name: Broad Institute Status API
  slug: broad-institute-status-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Submissions API from Broad Institute — 7 operation(s) for submissions.
  name: Broad Institute Submissions API
  slug: broad-institute-submissions-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Terms of Service API from Broad Institute — 4 operation(s) for terms of service.
  name: Broad Institute Terms of Service API
  slug: broad-institute-terms-of-service-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Users API from Broad Institute — 1 operation(s) for users.
  name: Broad Institute Users API
  slug: broad-institute-users-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Version API from Broad Institute — 2 operation(s) for version.
  name: Broad Institute Version API
  slug: broad-institute-version-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Womtool API from Broad Institute — 1 operation(s) for womtool.
  name: Broad Institute Womtool API
  slug: broad-institute-womtool-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The Workspaces API from Broad Institute — 20 operation(s) for workspaces.
  name: Broad Institute Workspaces API
  slug: broad-institute-workspaces-api
- baseURL: https://api.firecloud.org
  baseurl_source: declared
  description: The WorkspacesV2 API from Broad Institute — 8 operation(s) for workspacesv2.
  name: Broad Institute Workspaces V2 API
  slug: broad-institute-workspacesv2-api
artifact_total: 35
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/agentic-access/broad-institute-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/broad-institute-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/rules/broad-institute-rules.yml
  title: ''
  type: Spectral
  url: rules/broad-institute-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/json-ld/broad-institute-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/broad-institute-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/vocabulary/broad-institute-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/broad-institute-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/data-model/broad-institute-data-model.yml
  title: ''
  type: DataModel
  url: data-model/broad-institute-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/errors/broad-institute-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/broad-institute-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/conformance/broad-institute-conformance.yml
  title: ''
  type: Conformance
  url: conformance/broad-institute-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/hosts/broad-institute-hosts.yml
  title: ''
  type: Hosts
  url: hosts/broad-institute-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/vendors/broad-institute-vendors.yml
  title: ''
  type: Vendors
  url: vendors/broad-institute-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/packages/broad-institute-packages.yml
  title: ''
  type: SDKs
  url: packages/broad-institute-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/packages/broad-institute-packages.yml
  title: ''
  type: Packages
  url: packages/broad-institute-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/broadinstitute
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/scopes/broad-institute-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/broad-institute-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/authentication/broad-institute-authentication.yml
  title: ''
  type: Authentication
  url: authentication/broad-institute-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/broad-institute/refs/heads/main/security/broad-institute-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/broad-institute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.broadinstitute.org
created: '2026-10-14'
description: Broad Institute is a nonprofit biomedical research center dedicated to improving human health through advanced research, tool development, and open data sharing. It brings together a multidisciplinary community of scientists, engineers, and clinicians to accelerate discoveries and translate them into therapies, diagnostics, and public health solutions.
image: https://www.broadinstitute.org/themes/custom/broad/logo.png
json_schemas:
- name: ConfigurationResponse
  property_count: 13
  slug: broad-institute-configuration-response
- name: SubmissionRequest
  property_count: 13
  slug: broad-institute-submission-request
- name: Submission
  property_count: 15
  slug: broad-institute-submission
- name: Tool
  property_count: 13
  slug: broad-institute-tool
- name: WorkflowDescription
  property_count: 6
  slug: broad-institute-workflow-description
- name: WorkspaceDetails
  property_count: 19
  slug: broad-institute-workspace-details
jsonld:
- class_count: 120
  name: Broad Institute Context
  property_count: 280
  slug: broad-institute-context
layout: provider
modified: '2026-10-14'
name: Broad Institute
nav: Providers
network: true
overview: 'Broad Institute publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing V2 API, CromIAM Engine (for Job Manager) API, CromIAM Workflows (for Admin) API, and 20 more. Tagged areas include Biotechnology, Research, Genomics, Open Science, and Non-Profit.


  The Broad Institute catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Broad Institute''s developer surface includes authentication and 16 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Broad Institute API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 4
  slug: broad-institute-rules
scopes:
- name: Broad Institute Scopes
  scope_count: 0
  slug: broad-institute-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 53.4
    developer_ergonomics: 20.8
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 11.1
security:
- kind: authentication
  name: Broad Institute Authentication
  slug: broad-institute-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Broad Institute Domain Security
  slug: broad-institute-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: broad-institute
tags:
- Biotechnology
- Research
- Genomics
- Open Science
- Non-Profit
website: https://www.broadinstitute.org
---
