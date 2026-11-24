"""Shipping + return policy for Offer JSON-LD (Google "Záznamy obchodníka").

Digitální program v aplikaci Strivee: doručení zdarma a ihned, do celého světa.
Používá programs.py, pages.py, storefront_static.py i homepage (index.html).
"""
BASE = "https://str2g.com"
COUNTRIES = ("CZ", "SK", "DE", "AT", "PL", "FR", "ES", "IT", "NL", "BE", "GB", "IE", "US")
_DAY0 = {"@type": "QuantitativeValue", "minValue": 0, "maxValue": 0, "unitCode": "DAY"}
SHIPPING = {"@type": "OfferShippingDetails",
            "shippingRate": {"@type": "MonetaryAmount", "value": "0", "currency": "CZK"},
            "shippingDestination": [{"@type": "DefinedRegion", "addressCountry": c} for c in COUNTRIES],
            "deliveryTime": {"@type": "ShippingDeliveryTime", "handlingTime": _DAY0, "transitTime": _DAY0}}
RETURNS = {"@type": "MerchantReturnPolicy",
           "applicableCountry": list(COUNTRIES),
           "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted",
           "merchantReturnLink": BASE + "/refund-policy/"}


def add_merchant_fields(offer):
    """Doplní shippingDetails + hasMerchantReturnPolicy do Offer (dict), vrací ho zpět."""
    if offer.get("@type") == "Offer":
        offer.setdefault("shippingDetails", SHIPPING)
        offer.setdefault("hasMerchantReturnPolicy", RETURNS)
    return offer
