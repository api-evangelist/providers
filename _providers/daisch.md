---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: build
  href: https://artifacts.apis.io/daisch/packages/daisch-packages.yml
  title: ''
  type: SDKs
  url: packages/daisch-packages.yml
- group: build
  href: https://artifacts.apis.io/daisch/packages/daisch-packages.yml
  title: ''
  type: Packages
  url: packages/daisch-packages.yml
- group: other
  href: https://artifacts.apis.io/daisch/hosts/daisch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daisch-hosts.yml
- group: other
  href: https://artifacts.apis.io/daisch/vendors/daisch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daisch-vendors.yml
- group: auth
  href: https://artifacts.apis.io/daisch/security/daisch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daisch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daischsensor.com/
- group: company
  title: ''
  type: Blog
  url: https://daischsensor.com/category/blog/
- group: operate
  title: ''
  type: Support
  url: https://daischsensor.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daischsensor.com/daisch-sensor-privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DaischSensor
coverage:
  detail: DAISCH's own front door at daischsensor.com is open and readable (the prior bot-challenge verdict was recorded against the EquityZen venue listing, not the company itself). The company sells inertial-sensor hardware (IMU, GNSS/INS, AHRS modules and the IFS3000 ground-truth test system); no developer portal, OpenAPI specification, public API reference or MCP endpoint was found during the identity-pass probes. Open-source ROS 1 / ROS 2 drivers are published on the DaischSensor GitHub organization, which later modules may harvest for contracts.
  evidence:
  - status: 200
    url: https://daischsensor.com/
  - status: 200
    url: https://daischsensor.com/company-profile-imu-manufacturer/
  - status: 200
    url: https://github.com/DaischSensor
  - status: 403
    url: https://equityzen.com/company/daisch
  reason: not-a-software-company
  state: none
created: '2026-10-22'
description: DAISCH (Daisch Technology Co., Ltd.) is a Shanghai-based inertial sensing company founded in January 2015 that develops and manufactures high-precision IMU, GNSS/INS and AHRS sensors, motion-sensing modules, and the IFS3000 multi-vehicle networking ground-truth test system for ADAS and autonomous-vehicle validation. Its hardware is calibrated using the proprietary AutoCalix full-temperature calibration process, supported by DSX sensor-fusion software and the DS_RVision evaluation tool, and backed by IATF 16949, ISO 9001, ISO 26262 / ASIL D and Automotive SPICE certifications. Open-source ROS 1 and ROS 2 drivers for DAISCH IM1R sensors are published on the DaischSensor GitHub organization.
image: https://daischsensor.com/wp-content/uploads/2024/02/DAISCH-factory-1.webp
layout: provider
modified: '2026-11-03'
name: DAISCH
nav: Providers
network: true
overview: 'DAISCH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IMU, Inertial Measurement Unit, GNSS/INS, and AHRS.


  DAISCH''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 20
screenshot: https://apis.io/screenshots/daisch/daisch-2026-11-03T130014.png
security:
- kind: domain-security
  name: Daisch Domain Security
  slug: daisch-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: daisch
tags:
- Company
- IMU
- Inertial Measurement Unit
- GNSS/INS
- AHRS
- Motion Sensing
- Autonomous Driving
- ADAS
- Robotics
- Sensors
- Hardware Manufacturer
website: https://daischsensor.com/
---
