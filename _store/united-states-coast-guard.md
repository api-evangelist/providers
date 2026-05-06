---
aid: united-states-coast-guard
url: https://raw.githubusercontent.com/api-evangelist/united-states-coast-guard/refs/heads/main/apis.yml
apis:
  - aid: united-states-coast-guard:cgmix-maritime-information-exchange
    name: CGMIX Maritime Information Exchange API
    tags:
      - Maritime
      - Vessel Documentation
      - Safety
      - Federal Government
    humanURL: https://cgmix.uscg.mil/xml/default.aspx
    baseURL: https://cgmix.uscg.mil
    properties:
      - url: https://cgmix.uscg.mil/xml/default.aspx
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-coast-guard/refs/heads/main/openapi/cgmix-maritime-information-exchange-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-coast-guard/refs/heads/main/rules/cgmix-maritime-information-exchange-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-coast-guard/refs/heads/main/capabilities/maritime-safety.yaml
        type: NaftikoCapability
    description: The Coast Guard Maritime Information Exchange (CGMIX) provides XML web services for accessing Coast Guard maritime information including vessel documentation, Port State Information Exchange (PSIX) data, equipment certifications, and Incident Investigation Reports (IIR). Data originates from the Marine Information for Safety and Law Enforcement (MISLE) system and is updated weekly.
    contact:
      FN: U.S. Coast Guard
      url: https://cgmix.uscg.mil/
  - aid: united-states-coast-guard:navcen-ais-vessel-information
    name: NAVCEN AIS Vessel Information Verification Service
    tags:
      - Maritime
      - AIS
      - Vessel Tracking
      - Federal Government
    humanURL: https://www.navcen.uscg.gov/ais-vivs-home
    baseURL: https://www.navcen.uscg.gov
    properties:
      - url: https://www.navcen.uscg.gov/ais-vivs-home
        type: Documentation
      - url: https://www.navcen.uscg.gov/ais-vessel-information-verification-service
        type: Documentation
    description: The Vessel Information Verification Service (VIVS) is a NAVCEN web service that allows retrieval of a vessel's broadcasted AIS static data, including Maritime Mobile Service Identity (MMSI), call sign, vessel name, official number, dimensions, draft, vessel type, and positioning source. Provided by the U.S. Coast Guard Navigation Center.
name: United States Coast Guard
tags:
  - Federal Government
  - Maritime Safety
  - Vessel Documentation
  - Emergency Response
  - Law Enforcement
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: The United States Coast Guard is a branch of the military responsible for enforcing maritime laws, protecting the nation's waterways and coastlines, and ensuring the safety and security of seafarers. They conduct search and rescue operations, respond to environmental disasters, combat illegal drug trafficking and immigration, and conduct security patrols to thwart terrorism threats. The USCG provides public APIs and data services through the CGMIX Maritime Information Exchange, the Navigation Center (NAVCEN), and the National Vessel Documentation Center (NVDC).
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
