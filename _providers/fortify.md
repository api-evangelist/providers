---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 52.9
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 62
  human_in_the_loop: 1
  name: Fortify Agentic Access
  operation_count: 138
  slug: fortify-agentic-access
  summary_line: 138 operations · 62 acting · 1 human-in-the-loop
api_count: 42
apis:
- description: Manage alert definitions
  name: Fortify Alert Definitions API
  slug: fortify-alert-definitions-api
- description: Manage API keys for programmatic access
  name: Fortify API Keys API
  slug: fortify-api-keys-api
- description: Manage applications and their configurations
  name: Fortify Applications API
  slug: fortify-applications-api
- description: Manage scan artifacts and uploads
  name: Fortify Artifacts API
  slug: fortify-artifacts-api
- description: Manage application attributes
  name: Fortify Attributes API
  slug: fortify-attributes-api
- description: Manage audit templates for vulnerability triage
  name: Fortify Audit Templates API
  slug: fortify-audit-templates-api
- description: Manage authentication entities (users and LDAP groups)
  name: Fortify Auth Entities API
  slug: fortify-auth-entities-api
- description: Manage authentication tokens
  name: Fortify Authentication API
  slug: fortify-authentication-api
- description: CI/CD pipeline integration endpoints
  name: Fortify CI/CD API
  slug: fortify-ci-cd-api
- description: Manage cloud scan worker pools
  name: Fortify Cloud Pools API
  slug: fortify-cloud-pools-api
- description: Manage custom tags for issue triage
  name: Fortify Custom Tags API
  slug: fortify-custom-tags-api
- description: Configure and start DAST automated scans
  name: Fortify DAST Automated Scans API
  slug: fortify-dast-automated-scans-api
- description: Configure and start dynamic application security testing scans
  name: Fortify Dynamic Scans API
  slug: fortify-dynamic-scans-api
- description: Access tenant event logs
  name: Fortify Event Logs API
  slug: fortify-event-logs-api
- description: System feature and connectivity information
  name: Fortify Features API
  slug: fortify-features-api
- description: Manage file transfer tokens
  name: Fortify File Tokens API
  slug: fortify-file-tokens-api
- description: Retrieve issue filter metadata
  name: Fortify Issue Selectors API
  slug: fortify-issue-selectors-api
- description: Access and manage vulnerability issues
  name: Fortify Issues API
  slug: fortify-issues-api
- description: Monitor processing jobs
  name: Fortify Jobs API
  slug: fortify-jobs-api
- description: Retrieve lookup and reference data
  name: Fortify Lookup Items API
  slug: fortify-lookup-items-api
- description: Manage microservices within applications
  name: Fortify Microservices API
  slug: fortify-microservices-api
- description: Configure and start mobile application security testing scans
  name: Fortify Mobile Scans API
  slug: fortify-mobile-scans-api
- description: Manage user notifications
  name: Fortify Notifications API
  slug: fortify-notifications-api
- description: View open source component data
  name: Fortify Open Source Components API
  slug: fortify-open-source-components-api
- description: Manage open source / software composition analysis scans
  name: Fortify Open Source Scans API
  slug: fortify-open-source-scans-api
- description: Access performance indicator data
  name: Fortify Performance Indicators API
  slug: fortify-performance-indicators-api
- description: Manage personal access tokens
  name: Fortify Personal Access Tokens API
  slug: fortify-personal-access-tokens-api
- description: Manage application versions within projects
  name: Fortify Project Versions API
  slug: fortify-project-versions-api
- description: Manage top-level projects
  name: Fortify Projects API
  slug: fortify-projects-api
- description: Manage releases within applications
  name: Fortify Releases API
  slug: fortify-releases-api
- description: Generate and download reports
  name: Fortify Reports API
  slug: fortify-reports-api
- description: Manage saved report configurations
  name: Fortify Saved Reports API
  slug: fortify-saved-reports-api
- description: Manage scan policies
  name: Fortify Scan Policies API
  slug: fortify-scan-policies-api
- description: Manage scheduled scans
  name: Fortify Scan Schedules API
  slug: fortify-scan-schedules-api
- description: Manage scan configuration settings
  name: Fortify Scan Settings API
  slug: fortify-scan-settings-api
- description: View and manage security scans
  name: Fortify Scans API
  slug: fortify-scans-api
- description: Manage sensor pools for scan distribution
  name: Fortify Sensor Pools API
  slug: fortify-sensor-pools-api
- description: Manage WebInspect sensors
  name: Fortify Sensors API
  slug: fortify-sensors-api
- description: Configure and start static application security testing scans
  name: Fortify Static Scans API
  slug: fortify-static-scans-api
- description: System health and configuration
  name: Fortify System API
  slug: fortify-system-api
- description: Manage local user accounts
  name: Fortify Users API
  slug: fortify-users-api
- description: Access and manage vulnerability findings
  name: Fortify Vulnerabilities API
  slug: fortify-vulnerabilities-api
artifact_total: 65
collections:
- collection_type: open
  name: Fortify on Demand API
  slug: open-fortify-on-demand
- collection_type: open
  name: Fortify ScanCentral DAST API
  slug: open-fortify-scancentral-dast
- collection_type: open
  name: Fortify Software Security Center API
  slug: open-fortify-software-security-center
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fortify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fortify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fortify-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://ams.fortify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.microfocus.com/documentation/fortify-on-demand/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.microfocus.com/documentation/fortify-on-demand/
- group: auth
  title: ''
  type: Authentication
  url: https://api.ams.fortify.com/swagger/ui/index
- group: company
  title: ''
  type: Blog
  url: https://community.opentext.com/cyberres/b/cybersecurity-blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fortify.com/
- group: operate
  title: ''
  type: Support
  url: https://www.opentext.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opentext.com/about/legal/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opentext.com/about/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fortify
- group: operate
  title: ''
  type: Community
  url: https://community.opentext.com/cybersec/fortify
- group: company
  title: ''
  type: Website
  url: https://www.opentext.com/products/fortify-on-demand
- group: start
  title: ''
  type: Login
  url: https://ams.fortify.com/
- group: start
  title: ''
  type: Signup
  url: https://www.opentext.com/products/fortify-on-demand/trial
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.opentext.com/cybersec/fortify/w/tips
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fortify/fortify-client-api
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/fortify-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fortify-application-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fortify-vulnerability-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fortify-scan-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fortify-release-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fortify-project-version-schema.json
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/fortify/skills
created: '2024-01-15'
description: Fortify is a comprehensive application security platform from OpenText that provides static application security testing (SAST), dynamic application security testing (DAST), and software composition analysis (SCA) capabilities. It helps organizations identify and remediate vulnerabilities across the software development lifecycle.
finops:
- name: Fortify Finops
  service_category: Application Security
  slug: fortify-finops
image: https://www.microfocus.com/brand/fortify-logo.png
json_schemas:
- name: Fortify Application
  property_count: 10
  slug: fortify-application
- name: Fortify Project Version
  property_count: 11
  slug: fortify-project-version
- name: Fortify Release
  property_count: 19
  slug: fortify-release
- name: Fortify Scan
  property_count: 20
  slug: fortify-scan
- name: Fortify Vulnerability
  property_count: 24
  slug: fortify-vulnerability
jsonld:
- class_count: 0
  name: Fortify Context
  property_count: 11
  slug: fortify-context
layout: provider
modified: '2026-05-19'
name: Fortify
nav: Providers
network: true
overview: 'Fortify publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Alert Definitions API, API Keys API, Applications API, and 39 more. Tagged areas include Application Security, DAST, DevSecOps, SAST, and SCA.


  The Fortify catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fortify''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, signup flow, and 19 more developer resources.'
plans:
- name: Fortify Plans Pricing
  plan_count: 4
  slug: fortify-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Fortify Rate Limits
  slug: fortify-rate-limits
rules:
- name: Fortify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fortify-jsonschema-spectral-rules
score:
  band: strong
  composite: 65.1
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 67.2
    developer_ergonomics: 52.2
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 57.9
  previous_composite: 65.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/screenshots/fortify-2026-06-20T181440.png
security:
- kind: authentication
  name: Fortify Authentication
  slug: fortify-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Fortify Domain Security
  slug: fortify-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 7
skills:
- name: fcli-common
  slug: fcli-common
- name: fortify-cicd-integration
  slug: fortify-cicd-integration
- name: fortify-create-app
  slug: fortify-create-app
- name: fortify-exploitability-analysis
  slug: fortify-exploitability-analysis
- name: fortify-fod
  slug: fortify-fod
- name: fortify-remediate
  slug: fortify-remediate
- name: fortify-ssc
  slug: fortify-ssc
slug: fortify
tags:
- Application Security
- DAST
- DevSecOps
- SAST
- SCA
- Security Testing
- Vulnerability Scanning
website: https://www.opentext.com/products/fortify-on-demand
---
