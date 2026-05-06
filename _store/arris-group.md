---
aid: arris-group
url: https://raw.githubusercontent.com/api-evangelist/arris-group/refs/heads/main/apis.yml
name: ARRIS Group
tags:
  - Telecommunications
  - Broadband
  - Cable
  - Video
  - Networking
  - Equipment
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-19'
description: ARRIS Group was a global telecommunications equipment company providing entertainment and communications solutions including broadband, video, and wireless products for service providers and consumers. ARRIS was acquired by CommScope in 2019, combining their broadband technology expertise with CommScope's infrastructure solutions. The combined company offers cable modem equipment, set-top boxes, network infrastructure, DOCSIS technology, and related telecommunications hardware and software platforms for cable operators, telcos, and internet service providers worldwide.
apis:
  - aid: arris-group:commscope-api
    name: CommScope Developer API
    description: CommScope (formerly ARRIS) provides API and integration capabilities for network infrastructure management, including tools for managing broadband devices, DOCSIS networks, and cable plant equipment through their CommScope NBASE-T Alliance and related technology platforms.
    humanURL: https://www.commscope.com/
    baseURL: https://www.commscope.com
    tags:
      - Telecommunications
      - Broadband
      - Network Management
      - DOCSIS
    properties:
      - type: Documentation
        url: https://www.commscope.com/solutions/
common:
  - type: Portal
    url: https://www.commscope.com/
    title: CommScope Website (formerly ARRIS)
  - type: Documentation
    url: https://www.commscope.com/solutions/
    title: Solutions
  - type: Support
    url: https://www.commscope.com/support/
    title: Support
  - type: Features
    data:
      - name: DOCSIS Technology
        description: ARRIS/CommScope provides Data Over Cable Service Interface Specification (DOCSIS) technology enabling high-speed internet over cable infrastructure, including DOCSIS 3.1 and 3.0 modems and gateways.
      - name: Set-Top Box Platform
        description: Advanced set-top box products for cable operators enabling video delivery, content access, and interactive television services.
      - name: Network Infrastructure Management
        description: Software platforms for managing broadband access networks, including CMTS (Cable Modem Termination System) management and network analytics.
      - name: CCAP Architecture
        description: Converged Cable Access Platform technology converging CMTS and video-on-demand processing into a single platform.
  - type: UseCases
    data:
      - name: Broadband Network Deployment
        description: Cable operators use ARRIS/CommScope equipment to deploy and manage broadband internet infrastructure for residential and business customers.
      - name: Video Service Delivery
        description: Television service providers use ARRIS set-top boxes and headend equipment to deliver linear and on-demand video content to subscribers.
      - name: Network Operations
        description: Network operations teams use management software to monitor, configure, and troubleshoot broadband access networks and cable plant equipment.
  - type: Integrations
    data:
      - name: DOCSIS Standards
        description: ARRIS equipment integrates with CableLabs DOCSIS standards for interoperability across cable plant vendors and operators.
      - name: SCTE Standards
        description: Integration with Society of Cable Telecommunications Engineers (SCTE) standards for cable network operations and maintenance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
