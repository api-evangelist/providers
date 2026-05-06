---
aid: lf-connectivity
name: LF Connectivity
description: LF Connectivity is a Linux Foundation umbrella initiative, launched with Meta, that improves access to networks through open source projects. Sub-projects include Magma (a next-generation packet core), Terragraph (gigabit wireless last-mile access), Open M-Plane (RAN configuration and management), Maveric (AI/ML cellular network simulations), and the ISP Toolbox (planning and analytics for ISP operators).
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Connectivity
  - Linux Foundation
  - Networking
  - Telecom
  - Wireless
  - 5G
  - Open Source
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/lf-connectivity/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: lf-connectivity:magma
    name: Magma
    description: Magma is a next-generation packet core that delivers cellular network innovation at lower cost of ownership, with REST and gRPC APIs for orchestration, subscriber management, and policy enforcement.
    humanURL: https://magmacore.org/
    tags:
      - Packet Core
      - 5G
      - Cellular
      - Mobile Network
    properties:
      - type: Documentation
        url: https://magma.github.io/magma/docs/basics/introduction.html
      - type: GitHubRepo
        url: https://github.com/magma/magma
  - aid: lf-connectivity:terragraph
    name: Terragraph
    description: Terragraph is a wireless technology that enables internet service providers to deliver gigabit-speed last-mile access to homes, enterprises, and multi-dwelling buildings cost-effectively.
    humanURL: https://terragraph.com/
    tags:
      - Wireless
      - Last-Mile
      - Gigabit
      - Mesh
    properties:
      - type: Documentation
        url: https://terragraph.com/
      - type: GitHubOrg
        url: https://github.com/terragraph
  - aid: lf-connectivity:open-mplane
    name: Open M-Plane
    description: Open M-Plane is a software component of Meta's Evenstar hardware design for configuration and management of the Radio Access Network (RAN).
    humanURL: https://github.com/lf-connectivity/open-mplane
    tags:
      - RAN
      - Open RAN
      - Management
      - Configuration
    properties:
      - type: GitHubRepo
        url: https://github.com/lf-connectivity/open-mplane
  - aid: lf-connectivity:maveric
    name: Maveric
    description: Maveric is a platform that uses AI/ML to provide realistic cellular network simulations and reference examples demonstrating their use.
    humanURL: https://github.com/lf-connectivity/maveric
    tags:
      - AI
      - ML
      - Cellular Simulation
      - Network Modeling
    properties:
      - type: GitHubRepo
        url: https://github.com/lf-connectivity/maveric
  - aid: lf-connectivity:isp-toolbox
    name: ISP Toolbox
    description: ISP Toolbox empowers ISP operators with products, tools, and resources to better plan, analyze, and run their broadband businesses.
    humanURL: https://github.com/lf-connectivity/ISPToolbox
    tags:
      - ISP
      - Network Planning
      - Analytics
    properties:
      - type: GitHubRepo
        url: https://github.com/lf-connectivity/ISPToolbox
common:
  - type: Documentation
    name: LF Connectivity Documentation
    description: Official documentation for LF Connectivity.
    url: https://lfconnectivity.dev/
  - type: GitHubOrg
    name: LF Connectivity GitHub
    description: Source code and repositories for LF Connectivity.
    url: https://github.com/lf-connectivity
  - type: Website
    name: LF Connectivity Website
    description: Main LF Connectivity site.
    url: https://lfconnectivity.dev/
  - type: GitHubOrg
    name: Magma GitHub
    description: Magma packet core source code.
    url: https://github.com/magma
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
