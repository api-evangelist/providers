---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.5
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: CDEvents is a common specification for Continuous Delivery events that enables interoperability across CI/CD systems. It extends the CloudEvents specification and defines event vocabularies for source
  name: CDEvents Specification
  slug: cdevents
- baseURL_template: '{build_url}/stages'
  baseurl_source: spec_template
  description: Jenkins is the leading open source automation server, providing hundreds of plugins for building, deploying, and automating software projects. Jenkins exposes a remote access REST API that supports XM
  name: Jenkins
  slug: jenkins
- baseURL: http://localhost
  baseurl_source: spec
  description: 'Spinnaker is an open-source, multi-cloud continuous delivery platform originally built at Netflix and Google for releasing software changes with high velocity and confidence. Spinnaker exposes a Gate '
  name: Spinnaker
  slug: spinnaker
- baseURL: https://api.screwdriver.cd/
  baseurl_source: declared
  description: Screwdriver is an open-source build platform designed for Continuous Delivery, originally built at Yahoo. It provides a REST API for managing pipelines, builds, jobs, and webhooks and is designed to c
  name: Screwdriver
  slug: screwdriver
- description: Ortelius is an open source supply chain evidence store that aggregates continuous security intelligence across the software delivery lifecycle. It exposes APIs for tracking microservice components, SB
  name: Ortelius
  slug: ortelius
- description: JayeX is a customizable cloud developer tool suite hosted by the Continuous Delivery Foundation that provides built-in CI/CD capabilities and developer self-service tooling for cloud-native teams.
  name: JayeX
  slug: jayex
- description: The Continuous Delivery Foundation publishes a machine-readable index of its own website content. The foundation serves an RFC 9727 API catalog at /.well-known/api-catalog which anchors https://cd.fou
  name: CD Foundation Content API
  slug: content-api
- description: Tekton is a Kubernetes-native open source framework for creating CI/CD systems. It defines Custom Resource Definitions for Pipelines, Tasks, PipelineRuns, and TaskRuns and was originally hosted at the
  name: Tekton
  slug: tekton
artifact_total: 16
asyncapis:
- description: ''
  name: Continuous Delivery Foundation Cdevents Events
  slug: continuous-delivery-foundation-cdevents-events
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/continuous-delivery-foundation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/continuous-delivery-foundation-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/continuous-delivery-foundation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cdeliveryfdn
- group: company
  title: ''
  type: Website
  url: https://cd.foundation/
- group: other
  title: ''
  type: Projects
  url: https://cd.foundation/projects/
- group: docs
  title: ''
  type: Documentation
  url: https://cd.foundation/projects/
- group: company
  title: ''
  type: Blog
  url: https://cd.foundation/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://cd.foundation/news/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cdfoundation
- group: operate
  title: ''
  type: Community
  url: https://cd.foundation/community/
- group: other
  title: ''
  type: Events
  url: https://cd.foundation/events/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/continuous-delivery-foundation-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/continuous-delivery-foundation-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/continuous-delivery-foundation-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.jenkins.io/security/reporting/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/continuous-delivery-foundation-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/continuous-delivery-foundation-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/continuous-delivery-foundation-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/continuous-delivery-foundation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/continuous-delivery-foundation-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/continuous-delivery-foundation-cli.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/continuous-delivery-foundation-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/continuous-delivery-foundation-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/continuous-delivery-foundation-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jenkins.io/
- group: design
  title: ''
  type: Conventions
  url: conventions/continuous-delivery-foundation-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/continuous-delivery-foundation-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/continuous-delivery-foundation-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/continuous-delivery-foundation-cdevents-events.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/continuous-delivery-foundation-cdevents-schemas.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/continuous-delivery-foundation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/continuous-delivery-foundation-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/continuous-delivery-foundation-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/legal/privacy-policy
- group: learn
  title: ''
  type: Training
  url: https://cd.foundation/training/
- group: company
  title: ''
  type: Newsletter
  url: https://cd.foundation/newsletter/
created: '2026-03-16'
description: The Continuous Delivery Foundation (CDF) is a Linux Foundation project that hosts vendor-neutral open source projects for continuous integration, continuous delivery, and DevOps. It is the home of CDEvents, Jenkins, Spinnaker, Screwdriver, Ortelius, JayeX, and was previously the home of Tekton (now a CNCF graduated project) and other CD-focused tooling.
finops:
- name: Continuous Delivery Foundation Finops
  service_category: API
  slug: continuous-delivery-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/continuous-delivery-foundation.png
layout: provider
mcp_servers:
- description: ''
  name: Continuous Delivery Foundation MCP Server
  slug: continuous-delivery-foundation-mcp-server
modified: '2026-09-05'
name: Continuous Delivery Foundation
nav: Providers
network: true
overview: 'Continuous Delivery Foundation publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Jenkins, Spinnaker, Screwdriver, and 1 more. Tagged areas include Automation, CI/CD, DevOps, Linux Foundation, and Open-Source.


  The Continuous Delivery Foundation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Continuous Delivery Foundation''s developer surface includes authentication, documentation, engineering blog, CLI, changelog, training material, and 33 more developer resources.'
plans:
- name: Continuous Delivery Foundation Plans Pricing
  plan_count: 0
  slug: continuous-delivery-foundation-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Continuous Delivery Foundation Rate Limits
  slug: continuous-delivery-foundation-rate-limits
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 44.0
    catalog_earned_first_party: 6.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 64.9
    developer_ergonomics: 61.3
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 18.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/screenshots/continuous-delivery-foundation-2026-06-20T174948.png
security:
- kind: authentication
  name: Continuous Delivery Foundation Authentication
  slug: continuous-delivery-foundation-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Continuous Delivery Foundation Domain Security
  slug: continuous-delivery-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Continuous Delivery Foundation Vulnerability Disclosure
  slug: continuous-delivery-foundation-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: continuous-delivery-foundation
tags:
- Automation
- CI/CD
- DevOps
- Linux Foundation
- Open-Source
website: https://cd.foundation/
---
