from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]  # Allows for 1-20 items to be added to cart

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, 
        coerce=int,
        label='Quantity'
    )
    update = forms.BooleanField(
        required=False, 
        initial=False, 
        widget=forms.HiddenInput
    )