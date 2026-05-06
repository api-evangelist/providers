---
aid: ovh-cloud
name: OVH Cloud
description: OVH Cloud is a leading provider of cloud computing services that offer a wide range of solutions for businesses of all sizes. From virtual private servers and dedicated servers to storage, networking, and security services, OVH Cloud provides a comprehensive platform for organizations to build and deploy their applications and services in the cloud. With data centers located around the world, OVH Cloud offers high availability, scalability, and flexibility to meet the needs of its customers.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud
  - Compute
  - Servers
  - Hosting
created: '2024-04-18'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/ovh-cloud/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: ovh-cloud:ovh-cloud-api
    name: OVH Cloud API
    description: The OVHcloud API enables programmatic management of OVHcloud resources including dedicated servers, public cloud instances, storage, networking, Kubernetes, load balancers, container registries, databases, IP addressing, snapshots, SSH keys, billing operations, quotas, regions, and the vRack private network. It is the unified surface for automating the OVHcloud platform across compute, storage, network, and account lifecycle operations.
    humanURL: https://api.us.ovhcloud.com/console/?branch=v1
    baseURL: https://api.us.ovhcloud.com/v1
    tags:
      - Cloud
      - Compute
      - Servers
    properties:
      - type: Documentation
        url: https://help.ovhcloud.com/csm/en-api-getting-started-ovhcloud-api?id=kb_article_view&sysparm_article=KB0042777
      - type: OpenAPI
        url: openapi/ovh-cloud-openapi-original.yml
      - type: Console
        url: https://api.us.ovhcloud.com/console/?branch=v1
common:
  - type: Developer
    url: https://api.us.ovhcloud.com/
  - type: Status
    url: https://status.us.ovhcloud.com/
  - type: Blog
    url: https://us.ovhcloud.com/resources/blog/
  - type: Support
    url: https://us.ovhcloud.com/support/
  - type: CaseStudies
    url: https://us.ovhcloud.com/resources/case-studies/
  - type: Videos
    url: https://us.ovhcloud.com/videos/
  - type: Tutorials
    url: https://us.ovhcloud.com/community/tutorials/
  - type: UseCases
    url: https://us.ovhcloud.com/solutions/use-cases/
  - type: WhitePapers
    url: https://us.ovhcloud.com/resources/white-papers/
  - type: Glossary
    url: https://us.ovhcloud.com/glossary/
  - type: Login
    url: https://us.ovhcloud.com/auth/
  - type: Signup
    url: https://us.ovhcloud.com/auth/
  - type: Website
    url: https://us.ovhcloud.com/
  - type: About
    url: https://us.ovhcloud.com/about/
  - type: PressReleases
    url: https://us.ovhcloud.com/press/
  - type: TermsOfService
    url: https://us.ovhcloud.com/legal/terms-of-service/
  - type: PrivacyPolicy
    url: https://us.ovhcloud.com/legal/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
