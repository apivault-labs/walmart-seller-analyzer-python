"""Public exception hierarchy for the Walmart Seller Analyzer SDK."""

class WalmartSellerAnalyzerError(Exception):
    """Base SDK error."""

class AuthenticationError(WalmartSellerAnalyzerError):
    """The Apify token is missing or rejected."""

class ActorRunError(WalmartSellerAnalyzerError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(WalmartSellerAnalyzerError):
    """The client stopped waiting before the Actor completed."""
