const cheerio = require('cheerio');
const axios = require('axios')

const getAllMajors = async () => {
	try {
		const { data } = await axios.get(
			'https://students.ucsd.edu/academics/advising/majors-minors/undergraduate-majors.html'
		);
		const $ = cheerio.load(data);
		var allMajors = [];

		$('p, br :not(embed):not(strong):not(em):not(a)').each((_idx, el) => {
			const postTitle = $(el).text()
			allMajors.push(postTitle)
		});

        allMajors = allMajors.filter((a) => a);

		return allMajors;
	} catch (error) {
		throw error;
	}
};

getAllMajors()
.then((allMajors) => console.log(allMajors));
