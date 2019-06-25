from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:

    def test_self(self):
        adie = mixer.blend('adieup.Adie', orientation="queer")
        assert adie.__str__.orientation == "queer"
    
