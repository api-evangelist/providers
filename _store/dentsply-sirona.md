---
aid: dentsply-sirona
name: Dentsply Sirona
description: Dentsply Sirona is the world's largest manufacturer of professional dental products and technologies, providing comprehensive solutions for dentists, dental laboratories, and dental specialists worldwide. The company exposes developer integrations through DS Core, an open cloud platform, and through the Dentsply Sirona Imaging modality API for intraoral imaging hardware.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CAD/CAM
  - CEREC
  - Dental
  - DS Core
  - Imaging
  - Intraoral Imaging
  - Lab Management
  - Practice Management
url: https://raw.githubusercontent.com/api-evangelist/dentsply-sirona/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
position: Producer
access: 3rd-Party
apis:
  - aid: dentsply-sirona:ds-core-api
    name: DS Core API
    description: DS Core is the open cloud platform from Dentsply Sirona that connects dental practices, laboratories, and DSOs through a single web-based experience. The DS Core API enables Practice Management System (PMS) providers, Lab Management System (LMS) providers, and DSO enterprise solutions to integrate with DS Core for patient data synchronization, scan and imaging exchange, lab order routing, file and comment exchange, and Single Sign-On user provisioning.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://open.dscore.com/
    baseURL: https://api.dscore.com
    tags:
      - DS Core
      - Imaging
      - Lab Management
      - Patient Data
      - Practice Management
      - SSO
    properties:
      - type: Documentation
        url: https://open.dscore.com/
      - type: Sign Up
        url: https://open.dscore.com/
      - type: Marketing
        url: https://www.dentsplysirona.com/en/lp/connected-dentistry.html
    contact:
      - FN: DS Core Open Platform
        url: https://open.dscore.com/
  - aid: dentsply-sirona:dsio-modality-api
    name: Dentsply Sirona Intraoral Imaging Modality API
    description: The DSIO modality API enables third-party imaging software to drive Dentsply Sirona intraoral imaging hardware (sensors and cameras) through a documented protocol. The API and its reference client are published on GitHub by the Dentsply Sirona Imaging team and are intended for software vendors that wish to capture, transfer, and store intraoral images from Dentsply Sirona devices in their own dental software.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/dsimaging/dsio-modality-api
    baseURL: https://api.example.com
    tags:
      - GitHub
      - Imaging
      - Intraoral
      - Modality
      - Sensors
    properties:
      - type: Documentation
        url: https://github.com/dsimaging/dsio-modality-api
      - type: Source Code
        url: https://github.com/dsimaging/dsio-modality-api
    contact:
      - FN: Dentsply Sirona Imaging
        url: https://github.com/dsimaging
common:
  - type: Website
    url: https://www.dentsply-sirona.com
  - type: USA Website
    url: https://www.dentsplysirona.com/en-us
  - type: Open Platform
    url: https://open.dscore.com/
  - type: DS Core Marketing
    url: https://www.dentsplysirona.com/en-us/discover/discover-by-brand/ds-core.html
  - type: Connected Dentistry
    url: https://www.dentsplysirona.com/en/lp/connected-dentistry.html
  - type: Connect Software
    url: https://www.dentsplysirona.com/en-us/discover/discover-by-brand/connect-software.html
  - type: Service Portal
    url: https://service.dscore.com/
  - type: GitHub Imaging
    url: https://github.com/dsimaging
  - type: Investors
    url: https://investor.dentsplysirona.com
  - type: Newsroom
    url: https://www.dentsplysirona.com/en/about-dentsply-sirona/news.html
  - type: Sustainability
    url: https://www.dentsplysirona.com/en/about-dentsply-sirona/sustainability.html
  - type: Careers
    url: https://www.dentsplysirona.com/en/about-dentsply-sirona/careers.html
  - type: Contact
    url: https://www.dentsplysirona.com/en/about-dentsply-sirona/contact-us.html
  - type: Terms of Use
    url: https://www.dentsplysirona.com/en/legal-notice.html
  - type: Privacy Policy
    url: https://www.dentsplysirona.com/en/legal-notice/privacy-policy.html
  - type: JSON-LD
    url: json-ld/dentsply-sirona-context.jsonld
  - type: Vocabulary
    url: vocabulary/dentsply-sirona-vocabulary.yml
  - type: Capabilities
    url: capabilities/dentsply-sirona-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
