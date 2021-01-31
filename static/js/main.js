// After response from database is received
$(document).ajaxComplete(() => {
	// Initialise MaterializeCSS components
	$('.tooltipped').tooltip();
	$('.collapsible').collapsible({
		induration: 250,
		outduration: 250,
	});

	// Toast: confirm delete
	$('.confirm-delete-btn').on('click', () => showToast('deleted'));

	// Pagination: Go to page
	$('.page-link').on('click', (e) => goToPage(e.target.dataset.pageUrl));

	// Toast: 'Like'
	$('.thumb-anchor').on('click', () => showToast('liked'));

	// 'Delete' modal
	$('.modal').modal({ opacity: 0.2 });
	$('.delete-btn').on('click', (e) => {
		$('.confirm-delete-btn').attr(
			'href',
			'/delete_brew/' + e.target.dataset.id
		);
	});
});

$(document).ready(() => {
	// Get First page of results
	getFirstPage();

	// Toast: 'Updated'
	$('#update-brew-btn').on('click', () => showToast('updated'));

	// Toast: 'Added'
	$('#add-brew-btn').on('click', () => showToast('added'));

	// Display slider values for Add and Edit pages
	const SLIDER_VALUES = [
		'coffee_weight',
		'grind_size',
		'water_temp',
		'brew_time',
	];

	SLIDER_VALUES.forEach((sliderValue) => {
		displaySliderValue(sliderValue);
	});

	// On change of form, submit the form and reload the table
	$('#filters').on('change', () => getFirstPage());

	// Initialise Material components
	$('select').formSelect();
	$('.sidenav').sidenav();

	// Country input Autocomplete
	$('input.autocomplete').autocomplete({
		data: {
			Afghanistan: null,
			Albania: null,
			Algeria: null,
			Andorra: null,
			Angola: null,
			Anguilla: null,
			'Antigua &amp; Barbuda': null,
			Argentina: null,
			Armenia: null,
			Aruba: null,
			Australia: null,
			Austria: null,
			Azerbaijan: null,
			Bahamas: null,
			Bahrain: null,
			Bangladesh: null,
			Barbados: null,
			Belarus: null,
			Belgium: null,
			Belize: null,
			Benin: null,
			Bermuda: null,
			Bhutan: null,
			Bolivia: null,
			'Bosnia &amp; Herzegovina': null,
			Botswana: null,
			Brazil: null,
			'British Virgin Islands': null,
			Brunei: null,
			Bulgaria: null,
			'Burkina Faso': null,
			Burundi: null,
			Cambodia: null,
			Cameroon: null,
			'Cape Verde': null,
			'Cayman Islands': null,
			Chad: null,
			Chile: null,
			China: null,
			Colombia: null,
			Congo: null,
			'Cook Islands': null,
			'Costa Rica': null,
			'Cote D Ivoire': null,
			Croatia: null,
			Cuba: null,
			Cyprus: null,
			'Czech Republic': null,
			Denmark: null,
			Djibouti: null,
			Dominica: null,
			'Dominican Republic': null,
			Ecuador: null,
			Egypt: null,
			'El Salvador': null,
			'Equatorial Guinea': null,
			Estonia: null,
			Ethiopia: null,
			'Falkland Islands': null,
			'Faroe Islands': null,
			Fiji: null,
			Finland: null,
			France: null,
			'French Polynesia': null,
			'French West Indies': null,
			Gabon: null,
			Gambia: null,
			Georgia: null,
			Germany: null,
			Ghana: null,
			Gibraltar: null,
			Greece: null,
			Greenland: null,
			Grenada: null,
			Guam: null,
			Guatemala: null,
			Guernsey: null,
			Guinea: null,
			'Guinea Bissau': null,
			Guyana: null,
			Haiti: null,
			Honduras: null,
			'Hong Kong': null,
			Hungary: null,
			Iceland: null,
			India: null,
			Indonesia: null,
			Iran: null,
			Iraq: null,
			Ireland: null,
			'Isle of Man': null,
			Israel: null,
			Italy: null,
			Jamaica: null,
			Japan: null,
			Jersey: null,
			Jordan: null,
			Kazakhstan: null,
			Kenya: null,
			Kuwait: null,
			'Kyrgyz Republic': null,
			Laos: null,
			Latvia: null,
			Lebanon: null,
			Lesotho: null,
			Liberia: null,
			Libya: null,
			Liechtenstein: null,
			Lithuania: null,
			Luxembourg: null,
			Macau: null,
			Macedonia: null,
			Madagascar: null,
			Malawi: null,
			Malaysia: null,
			Maldives: null,
			Mali: null,
			Malta: null,
			Mauritania: null,
			Mauritius: null,
			Mexico: null,
			Moldova: null,
			Monaco: null,
			Mongolia: null,
			Montenegro: null,
			Montserrat: null,
			Morocco: null,
			Mozambique: null,
			Namibia: null,
			Nepal: null,
			Netherlands: null,
			'Netherlands Antilles': null,
			'New Caledonia': null,
			'New Zealand': null,
			Nicaragua: null,
			Niger: null,
			Nigeria: null,
			Norway: null,
			Oman: null,
			Pakistan: null,
			Palestine: null,
			Panama: null,
			'Papua New Guinea': null,
			Paraguay: null,
			Peru: null,
			Philippines: null,
			Poland: null,
			Portugal: null,
			'Puerto Rico': null,
			Qatar: null,
			Reunion: null,
			Romania: null,
			Russia: null,
			Rwanda: null,
			'Saint Pierre &amp; Miquelon': null,
			Samoa: null,
			'San Marino': null,
			Satellite: null,
			'Saudi Arabia': null,
			Senegal: null,
			Serbia: null,
			Seychelles: null,
			'Sierra Leone': null,
			Singapore: null,
			Slovakia: null,
			Slovenia: null,
			'South Africa': null,
			'South Korea': null,
			Spain: null,
			'Sri Lanka': null,
			'St Kitts &amp; Nevis': null,
			'St Lucia': null,
			'St Vincent': null,
			'St. Lucia': null,
			Sudan: null,
			Suriname: null,
			Swaziland: null,
			Sweden: null,
			Switzerland: null,
			Syria: null,
			Taiwan: null,
			Tajikistan: null,
			Tanzania: null,
			Thailand: null,
			"Timor L'Este": null,
			Togo: null,
			Tonga: null,
			'Trinidad &amp; Tobago': null,
			Tunisia: null,
			Turkey: null,
			Turkmenistan: null,
			'Turks &amp; Caicos': null,
			Uganda: null,
			Ukraine: null,
			'United Arab Emirates': null,
			'United Kingdom': null,
			USA: null,
			Uruguay: null,
			Uzbekistan: null,
			Venezuela: null,
			Vietnam: null,
			'Virgin Islands (US)': null,
			Yemen: null,
			Zambia: null,
			Zimbabwe: null,
		},
	});
});

// Displays value of slider in Add Brew & Edit Brew pages
const displaySliderValue = (slider_name) => {
	const sliderNameValue = $(`input[name="${slider_name}"]`).val();
	$(`#${slider_name}_span`).text(`${sliderNameValue}`);
};

// on click or touchend (touch screens) of input slider, call displaySliderValue
$('.input-slider').on('change' || 'touchend', (e) =>
	displaySliderValue(e.target.name)
);

// Request first page of brews from database
const getFirstPage = () => {
	// Get filters from form
	let serialFilters = $('#filters').serialize();
	// Ajax Get Request
	const firstPageUrl = '/get_brews?' + serialFilters;

	$.ajax({
		url: firstPageUrl,
		type: 'GET',
		success: (resp) => {
			// Insert response into response id
			$('#response').html(resp.data);
		},
	});
};

// Pagination: request brews for page
const goToPage = (urlPage) => {
	// Ajax get request
	$.ajax({
		url: urlPage,
		type: 'GET',
		success: (resp) => {
			// Insert response insto response id
			$('#response').html(resp.data);
		},
	});
};

// Show toast notification
const showToast = (toastEvent) => {
	let toastHtml = '';
	switch (toastEvent) {
		case 'deleted':
			toastHtml = `Deleted &nbsp; <i class="material-icons bin">delete</i>`;
			break;
		case 'added':
			toastHtml = `Brew Added &nbsp; <i class="material-icons">add_circle</i>`;
			break;
		case 'updated':
			toastHtml = `Brew Updated &nbsp; <i class="material-icons pencil">edit</i>`;
			break;
		case 'liked':
			toastHtml = `Liked &nbsp; <i class="material-icons thumb">thumb_up</i>`;
			break;
		default:
			break;
	}
	M.toast({
		html: toastHtml,
		classes: 'rounded',
	});
};
