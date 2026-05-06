---
aid: amerco
name: AMERCO
description: AMERCO, operating as U-Haul Holding Company, is America's largest do-it-yourself moving and storage company. The company provides truck and trailer rentals, self-storage facilities, moving supplies, and portable moving and storage containers through its U-Haul brand. AMERCO operates the Moving Help marketplace connecting consumers to moving service providers, the U-Haul Self-Storage Affiliate Network, and WebSelfStorage management software for independent storage facilities. It also operates AMERITAS Life Insurance and Oxford Life Insurance subsidiaries.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Moving
  - Storage
  - Truck Rental
  - Logistics
  - Consumer Services
url: https://raw.githubusercontent.com/api-evangelist/amerco/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amerco:uhaul
    name: U-Haul
    description: U-Haul provides do-it-yourself moving and storage services including truck and trailer rentals, self-storage, moving supplies, and U-Box portable storage containers. Partners access dealer management tools via the U-Haul dealer portal and self-storage affiliates use WebSelfStorage management software.
    humanURL: https://www.uhaul.com/
    baseURL: https://www.uhaul.com
    tags:
      - Moving
      - Storage
      - Truck Rental
      - Dealer Program
    properties:
      - type: Documentation
        url: https://www.uhaul.com/
      - type: Portal
        url: https://www.uhaul.com/Dealer/
common:
  - type: Website
    url: https://www.amerco.com/
  - type: Website
    url: https://www.uhaul.com/
  - type: Portal
    url: https://www.uhaul.com/Dealer/
  - type: Features
    data:
      - name: Truck and Trailer Rental Network
        description: Nationwide network of U-Haul trucks and trailers available through dealer locations with online booking and 24/7 customer support.
      - name: Self-Storage Facilities
        description: U-Haul owned and affiliate self-storage facilities with online reservation management and climate-controlled options.
      - name: Moving Help Marketplace
        description: Online marketplace connecting consumers to independent moving service providers for loading, unloading, packing, and cleaning services.
      - name: U-Haul Self-Storage Affiliate Network
        description: Partner network for independent self-storage facilities to list inventory and accept reservations through uhaul.com with WebSelfStorage management software.
      - name: WebSelfStorage Management Software
        description: Self-storage management application providing reservation management, tenant tracking, payment processing, and reporting for independent storage facilities.
      - name: U-Box Portable Storage
        description: Portable moving and storage container service with pickup, transport, and delivery options for local and long-distance moves.
      - name: Dealer Program
        description: No-investment dealer program for small businesses to add U-Haul truck and trailer rental to existing product offerings with 21% average commission and weekly direct deposit payments.
  - type: UseCases
    data:
      - name: Local and Long-Distance Moving
        description: Individuals and families rent trucks and trailers for DIY residential and commercial moves across the U-Haul network.
      - name: Self-Storage Management
        description: Independent storage facility owners manage reservations, payments, and tenant accounts through WebSelfStorage software.
      - name: Moving Service Provider Marketplace
        description: Independent movers offer loading, unloading, and packing services through the Moving Help marketplace on uhaul.com.
      - name: Dealer Business Revenue
        description: Small businesses add U-Haul rental services to generate supplemental revenue with zero startup costs and high commissions.
  - type: Integrations
    data:
      - name: Moving Help Marketplace
        description: Platform integration connecting consumers to independent moving service providers nationwide through uhaul.com.
      - name: AMERITAS Life Insurance
        description: AMERCO subsidiary providing life insurance products as part of the broader AMERCO financial services portfolio.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
