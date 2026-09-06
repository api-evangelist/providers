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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Cloud Foundry Agentic Access
  operation_count: 29
  slug: cloud-foundry-agentic-access
  summary_line: 29 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Cloud Controller API (CAPI) v3 is the primary control plane of Cloud Foundry. It manages apps, packages, droplets, builds, deployments, processes, tasks, revisions, routes, domains, organizations,
  name: Cloud Foundry Cloud Controller API v3
  slug: capi-v3
- description: The User Account and Authentication (UAA) server is Cloud Foundry's identity provider and OAuth 2.0 authorization server. It issues tokens consumed by the Cloud Controller, brokers, and operator tooli
  name: Cloud Foundry UAA
  slug: uaa
- description: Loggregator is Cloud Foundry's distributed log and metric pipeline that aggregates application logs, platform component logs, and metrics for streaming consumption by users and external sinks. It expo
  name: Cloud Foundry Loggregator
  slug: loggregator
- baseURL: https://{broker-host}
  baseurl_source: declared
  description: The Open Service Broker API is the open specification originally developed by Cloud Foundry and now used by Kubernetes and other platforms to provision and manage backing services through a common HTT
  name: Open Service Broker API
  slug: open-service-broker-api
- description: BOSH is Cloud Foundry's release engineering tool for packaging, deploying, and managing distributed software. The BOSH Director API exposes deployment, stemcell, release, task, and VM lifecycle operat
  name: BOSH Director API
  slug: bosh
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Apps API from Cloud Foundry — 4 operation(s) for apps.
  name: Cloud Foundry Apps API
  slug: cloud-foundry-apps-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Builds API from Cloud Foundry — 1 operation(s) for builds.
  name: Cloud Foundry Builds API
  slug: cloud-foundry-builds-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Cloud Foundry Cloud Controller API V3 API from Cloud Foundry — 2 operation(s) for cloud foundry cloud controller api v3.
  name: Cloud Foundry Cloud Foundry Cloud Controller API V3 API
  slug: cloud-foundry-cloud-foundry-cloud-controller-api-v3-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Deployments API from Cloud Foundry — 1 operation(s) for deployments.
  name: Cloud Foundry Deployments API
  slug: cloud-foundry-deployments-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Jobs API from Cloud Foundry — 1 operation(s) for jobs.
  name: Cloud Foundry Jobs API
  slug: cloud-foundry-jobs-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Organizations API from Cloud Foundry — 2 operation(s) for organizations.
  name: Cloud Foundry Organizations API
  slug: cloud-foundry-organizations-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Service Instances API from Cloud Foundry — 2 operation(s) for service instances.
  name: Cloud Foundry Service Instances API
  slug: cloud-foundry-service-instances-api
- baseURL: https://api.{system-domain}
  baseurl_source: declared
  description: The Spaces API from Cloud Foundry — 2 operation(s) for spaces.
  name: Cloud Foundry Spaces API
  slug: cloud-foundry-spaces-api
- baseURL: https://{autoscaler-api-server-url}
  baseurl_source: declared
  description: The App Autoscaler is a Cloud Foundry service that automatically scales application instances against dynamic metric rules and scheduled windows. The project publishes OpenAPI descriptions for its pub
  name: Cloud Foundry App Autoscaler API
  slug: app-autoscaler
artifact_total: 34
asyncapis:
- description: ''
  name: Cloud Foundry Event Surface
  slug: cloud-foundry-event-surface
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps API
  slug: open-cloud-foundry-apps-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Builds API
  slug: open-cloud-foundry-builds-api
- collection_type: open
  name: Apps Cloud Foundry Cloud Controller API V3 API
  slug: open-cloud-foundry-cloud-foundry-cloud-controller-api-v3-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Deployments API
  slug: open-cloud-foundry-deployments-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Jobs API
  slug: open-cloud-foundry-jobs-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Organizations API
  slug: open-cloud-foundry-organizations-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Service Instances API
  slug: open-cloud-foundry-service-instances-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3 Apps Spaces API
  slug: open-cloud-foundry-spaces-api
- collection_type: open
  name: Cloud Foundry Cloud Controller API v3
  slug: open-cloud-foundry
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloud-foundry-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloud-foundry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloud-foundry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloud-foundry-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloud-foundry
- group: company
  title: ''
  type: Website
  url: https://www.cloudfoundry.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudfoundry.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudfoundry
- group: other
  title: ''
  type: Foundation
  url: https://www.cloudfoundry.org/foundation/
- group: operate
  title: ''
  type: Community
  url: https://www.cloudfoundry.org/community/
- group: company
  title: ''
  type: Blog
  url: https://www.cloudfoundry.org/blog/
- group: other
  title: ''
  type: Events
  url: https://www.cloudfoundry.org/events/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/privacy
- group: other
  title: ''
  type: Trademark
  url: https://www.linuxfoundation.org/trademark-usage
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloud-foundry-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloud-foundry-rules.yml
- group: operate
  title: ''
  type: Slack
  url: https://cloudfoundry.slack.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudfoundry.org/terms/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cloudfoundry.org/
- group: docs
  title: ''
  type: APIReference
  url: https://v3-apidocs.cloudfoundry.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudfoundry.org/cf-cli/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudfoundry
- group: operate
  title: ''
  type: Support
  url: https://www.cloudfoundry.org/community/
- group: build
  title: ''
  type: Packages
  url: packages/cloud-foundry-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloud-foundry-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cloud-foundry-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloud-foundry-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cloud-foundry-capi-v3-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloud-foundry-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloud-foundry-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloud-foundry-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cloud-foundry-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloud-foundry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/cloud-foundry-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloud-foundry-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cloud-foundry-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloud-foundry-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloud-foundry-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloud-foundry-rate-limits.yml
- group: build
  title: ''
  type: PostmanCollection
  url: collections/cloud-foundry.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/cloud-foundry.opencollection.json
- group: other
  title: ''
  type: EventSurface
  url: asyncapi/cloud-foundry-event-surface.yml
created: '2024-01-01'
description: Cloud Foundry is an open-source, multi-cloud Platform as a Service (PaaS) governed by the Cloud Foundry Foundation. It provides a developer-friendly application platform where operators push source code or container images and Cloud Foundry handles staging, routing, scaling, and lifecycle management. The CF API (api.cloudfoundry.org) is the primary control plane and is documented at v3.cloudfoundry.org/version/release-candidate. The ecosystem also includes the User Account and Authentication (UAA) OAuth 2.0 server, the Loggregator log and metric pipeline, the Diego container scheduler, the Open Service Broker API for marketplace services, and the Eirini Kubernetes-based scheduler.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloud-foundry.png
jsonld:
- class_count: 0
  name: Cloud Foundry Context
  property_count: 11
  slug: cloud-foundry-context
layout: provider
modified: '2026-09-05'
name: Cloud Foundry
nav: Providers
network: true
overview: 'Cloud Foundry publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Cloud Controller API v3, Open Service Broker API, Apps API, and 8 more. Tagged areas include Cloud Foundry Foundation, Containers, Multi-Cloud, Open-Source, and Platform-as-a-Service.


  The Cloud Foundry catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cloud Foundry''s developer surface includes authentication, documentation, GitHub presence, engineering blog, API reference, getting-started guide, support, and 36 more developer resources.'
plans:
- name: Cloud Foundry Plans Pricing
  plan_count: 0
  slug: cloud-foundry-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Cloud Foundry Rate Limits
  slug: cloud-foundry-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Cloud Foundry API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: cloud-foundry-rules
scopes:
- name: Cloud Foundry Scopes
  scope_count: 7
  slug: cloud-foundry-scopes
  summary_line: 7 scopes · implicit
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 22.4
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 72.7
    contract_quality: 62.4
    developer_ergonomics: 74.4
    discoverability: 75.9
    governance: 72.7
    operational_transparency: 36.8
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 69.2
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cloud-foundry/refs/heads/main/screenshots/cloud-foundry-2026-06-20T174548.png
security:
- kind: authentication
  name: Cloud Foundry Authentication
  slug: cloud-foundry-authentication
  summary_line: http/mutualTLS/oauth2 · 4 schemes
- kind: domain-security
  name: Cloud Foundry Domain Security
  slug: cloud-foundry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloud Foundry Vulnerability Disclosure
  slug: cloud-foundry-vulnerability-disclosure
  summary_line: disclosure policy published
slug: cloud-foundry
tags:
- Cloud Foundry Foundation
- Containers
- Multi-Cloud
- Open-Source
- Platform-as-a-Service
- Platform
website: https://www.cloudfoundry.org/
---
