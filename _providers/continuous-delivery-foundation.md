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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: CDEvents is a common specification for Continuous Delivery events that enables interoperability across CI/CD systems. It extends the CloudEvents specification and defines event vocabularies for source
  name: CDEvents Specification
  slug: cdevents
- description: Jenkins is the leading open source automation server, providing hundreds of plugins for building, deploying, and automating software projects. Jenkins exposes a remote access REST API that supports XM
  name: Jenkins
  slug: jenkins
- description: 'Spinnaker is an open-source, multi-cloud continuous delivery platform originally built at Netflix and Google for releasing software changes with high velocity and confidence. Spinnaker exposes a Gate '
  name: Spinnaker
  slug: spinnaker
- description: Screwdriver is an open-source build platform designed for Continuous Delivery, originally built at Yahoo. It provides a REST API for managing pipelines, builds, jobs, and webhooks and is designed to c
  name: Screwdriver
  slug: screwdriver
- description: Ortelius is an open source supply chain evidence store that aggregates continuous security intelligence across the software delivery lifecycle. It exposes APIs for tracking microservice components, SB
  name: Ortelius
  slug: ortelius
- description: JayeX is a customizable cloud developer tool suite hosted by the Continuous Delivery Foundation that provides built-in CI/CD capabilities and developer self-service tooling for cloud-native teams.
  name: JayeX
  slug: jayex
- description: Tekton is a Kubernetes-native open source framework for creating CI/CD systems. It defines Custom Resource Definitions for Pipelines, Tasks, PipelineRuns, and TaskRuns and was originally hosted at the
  name: Tekton
  slug: tekton
artifact_total: 11
common:
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
created: '2026-03-16'
description: The Continuous Delivery Foundation (CDF) is a Linux Foundation project that hosts vendor-neutral open source projects for continuous integration, continuous delivery, and DevOps. It is the home of CDEvents, Jenkins, Spinnaker, Screwdriver, Ortelius, JayeX, and was previously the home of Tekton (now a CNCF graduated project) and other CD-focused tooling.
finops:
- name: Continuous Delivery Foundation Finops
  service_category: API
  slug: continuous-delivery-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/continuous-delivery-foundation.png
layout: provider
modified: '2026-04-28'
name: Continuous Delivery Foundation
nav: Providers
network: true
overview: 'Continuous Delivery Foundation publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, CI/CD, DevOps, Linux Foundation, and Open-Source.


  Continuous Delivery Foundation''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Continuous Delivery Foundation Plans Pricing
  plan_count: 3
  slug: continuous-delivery-foundation-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Continuous Delivery Foundation Rate Limits
  slug: continuous-delivery-foundation-rate-limits
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 18.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/screenshots/continuous-delivery-foundation-2026-06-20T174948.png
security:
- kind: domain-security
  name: Continuous Delivery Foundation Domain Security
  slug: continuous-delivery-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: continuous-delivery-foundation
tags:
- Automation
- CI/CD
- DevOps
- Linux Foundation
- Open-Source
website: https://cd.foundation/
---
