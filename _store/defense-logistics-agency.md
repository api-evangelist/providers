---
aid: defense-logistics-agency
name: Defense Logistics Agency
description: The Defense Logistics Agency (DLA) is the U.S. Department of Defense combat support agency that manages a global supply chain spanning roughly five million items in nine supply chains plus storage, distribution, fuel, construction, and disposition missions. DLA operates an extensive catalog of business applications used by suppliers, the military services, and federal partners. Most DLA applications require account registration and operate behind authentication; public-facing surfaces include the DLA Internet Bid Board System (DIBBS), the DLA Disposition Services storefront, the FedMall procurement marketplace, and federated logistics search tools.
url: https://raw.githubusercontent.com/api-evangelist/defense-logistics-agency/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
xType: government
access: 3rd-Party
position: Consuming
tags:
  - Acquisition
  - Defense
  - Department of Defense
  - DLA
  - Federal Government
  - Logistics
  - Procurement
  - Supply Chain
created: '2024-12-03'
modified: '2026-04-28'
apis:
  - aid: defense-logistics-agency:defense-logistics-agency-applications
    name: DLA Applications Catalog
    description: Comprehensive list of DLA business applications used to work with the agency, including supply, contracting, distribution, disposition, fuel, and energy systems. The catalog provides links, contacts, and outage notices but does not itself expose a developer API.
    humanURL: https://www.dla.mil/Working-With-DLA/Applications
    tags:
      - Applications
      - Catalog
    properties:
      - type: Documentation
        url: https://www.dla.mil/Working-With-DLA/Applications
  - aid: defense-logistics-agency:defense-logistics-agency-dibbs
    name: DLA Internet Bid Board System (DIBBS)
    description: Web-based application used by the Defense Logistics Agency to post requests for quote, solicitations, awards, and modifications for contracted supplies. Suppliers register for accounts and respond to solicitations through the DIBBS portal.
    humanURL: https://www.dibbs.bsm.dla.mil
    tags:
      - Bidding
      - Contracting
      - Procurement
      - Solicitations
    properties:
      - type: Documentation
        url: https://www.dibbs.bsm.dla.mil
  - aid: defense-logistics-agency:defense-logistics-agency-disposition-services
    name: DLA Disposition Services
    description: Online presence and storefronts for DLA Disposition Services that handle the reuse, transfer, donation, sale, and disposal of excess Department of Defense property, including the GovPlanet sales partnership and the LSDDS data services for property tracking.
    humanURL: https://www.dla.mil/Disposition-Services
    tags:
      - Disposal
      - Property
      - Reuse
      - Sales
    properties:
      - type: Documentation
        url: https://www.dla.mil/Disposition-Services
  - aid: defense-logistics-agency:defense-logistics-agency-fedmall
    name: FedMall
    description: DoD procurement marketplace operated by DLA where authorized buyers from federal, state, local, tribal, and authorized contractor communities purchase commercial off-the-shelf goods. FedMall provides catalog ingestion and order management interfaces for participating suppliers.
    humanURL: https://www.fedmall.mil
    tags:
      - eCommerce
      - Marketplace
      - Procurement
    properties:
      - type: Documentation
        url: https://www.fedmall.mil
  - aid: defense-logistics-agency:defense-logistics-agency-energy
    name: DLA Energy
    description: DLA business unit that supplies fuel and aerospace energy products to the U.S. military and federal customers. Public-facing surfaces include the Energy customer portal and contracting bulletins.
    humanURL: https://www.dla.mil/Energy
    tags:
      - Aerospace
      - Energy
      - Fuel
    properties:
      - type: Documentation
        url: https://www.dla.mil/Energy
common:
  - type: Website
    url: https://www.dla.mil
  - type: Documentation
    url: https://www.dla.mil/Working-With-DLA/Applications
  - type: News
    url: https://www.dla.mil/News
  - type: ContactUs
    url: https://www.dla.mil/Contact
  - type: PrivacyPolicy
    url: https://www.dla.mil/Site-Notices/Privacy-and-Security
  - type: FOIA
    url: https://www.dla.mil/Info/FOIA
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
