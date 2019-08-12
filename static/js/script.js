$(document).ready(function(){
	var form = $('.form_buying_product');
	//var form = $( event.target ).closest('.form_buying_product');
	
	function cartUpdating(product_id, image_url, nmb, is_delete){
		var data = {};
		data.product_id = product_id;
		data.nmb = nmb;
		data.image_url = image_url;
		//data.price = price;
		
		var csrf_token = $('.form_buying_product [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		
		if (is_delete){
			data["is_delete"] = true;
		}
		
		var url = form.attr("action");
				
		console.log(data)
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function (data) {
				console.log("OK");
				if (data.products_total_nmb || data.products_total_nmb == 0){
					$('#cart_total_nmb').text("("+data.products_total_nmb+")");
					//console.log(data.products);
					$('.cart-items').html("");
					var checkout_lnk = document.getElementById('checkout_lnk_href').getAttribute('value');
					console.log(checkout_lnk);
					$('.cart-items').html('<a id="checkout_lnk" href="'+checkout_lnk+'">MAKE THE ORDER</a> ');
					$.each(data.products, function(k, v){
						$('.cart-items').append('<pre><img class="img-micro" src="'+ v.image_url +'"><a>' + v.name + '  x'+ v.nmb + ' by $' + v.price_per_item + ' = $' + v.total_price +'<a class="delete-item" href="#" data-product_id="'+v.id+'"> X </a></pre></a>');
						
					});
				}
			},
			error: function(){
				console.log("error")
			}
		});
	}
	
	
	$('.order').not('bot_pm').on('click', function(e){
		//$('.order').not('.client').on('change', function() {
		e.preventDefault();


			var $self = $(this);
			var orderItem = $self.closest('.order');
			var product_id = $self.data("product_id");
			if ($('#'+product_id).val()){
				var nmb = $('#'+product_id).val();
			}else{
				var nmb = '1';
			};
			var name = $self.data("name");
			var image_url = $self.data("image_url");
	
		cartUpdating(product_id, image_url, nmb, is_delete=false)
				
	});
	
	function showingCart(){
		var cartAmount = cart_total_nmb.innerHTML;
		cartAmount = cartAmount.trim();
		//console.log(cartAmount);
		if (cartAmount != "(0)"){
			$('.put').addClass('show');
		};
	};
	
	// $('.cart-container').on('click', function(e){
		// e.preventDefault();
		// showingCart();
	// });
	
	$('.cart-container').mouseover(function(){
		showingCart();
		
	});
	
	$('.dropdown-menu').mouseout(function(){
		$('.put').removeClass('show');	
	});
	
	$(document).on('click', '.delete-item', function(e){
		e.preventDefault();
		product_id = $(this).data("product_id");
		nmb = 0;
		image_url = $(this).data("image_url");
		cartUpdating(product_id, image_url, nmb, is_delete=true)
		$(this).closest('a').remove();
	});
	
	function calculatingCartAmount(){
		var checkout_total_order_amount = 0;
		$('.checkout-total-product-price').each(function(){
			checkout_total_order_amount += parseFloat($(this).text());
		});
		
		$('#checkout_total_order_amount').text(parseFloat(checkout_total_order_amount).toFixed(2));
	};
	
	$(document).on('change', ".checkout-product-nmb", function(){
		var current_nmb = $(this).val();
		
		var current_tr = $(this).closest('tr');
		var current_price = parseFloat(current_tr.find('.checkout-product-price').text()).toFixed(2);
		var total_amount = parseFloat(current_nmb * current_price).toFixed(2);
		current_tr.find('.checkout-total-product-price').text(total_amount);
		calculatingCartAmount();
	});
	
	calculatingCartAmount();
});