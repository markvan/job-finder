class IndeedJobFormatter:

    # job that is being passed around is a beautiful soup object

    @staticmethod
    def format(job):
        out = "<div class='job'>"
        out += IndeedJobFormatter._heading(job)
        # out += '<div class="notes">'
        # out += '<div class="textbox">'
        # out += '<p class="alignleft">' + IndeedJobFormatter._salary(job) + '</p>'
        # out += '<p class="alignright">' + IndeedJobFormatter._date_posted(job) + '</p>'
        # out += '</div><div style="clear: both;"></div>'
        # out += '<p>' + IndeedJobFormatter._location(job) + '</p>'
        # out += '</div>'
        out += IndeedJobFormatter._description(job)
        out += "</div>"
        out = out.replace('...', "").replace('…', "").replace('  ', ' ').replace(" ", ' ')
        # TODO messy clean up
        out = out.replace('<br/><br/>', '<br/>').replace('<br/> <br/>', '<br/>').replace('<p><p/>', "")
        return out

    @staticmethod
    def _heading(job):
        a_tag = job.find('a')
        href = a_tag['href']
        href = href.replace('/rc/clk?', 'https://www.indeed.co.uk/viewjob?')
        out = '<h2><a href="' + href + '" target="_blank" rel="noopener noreferrer" >' + str(a_tag.contents[0]) + '</a></h2>'
        return out

    @staticmethod
    def _description(job):
        out = '<div class ="job-description-indeed">'
        out += job.find('span', class_='summary').text
        out += '</div>'
        return out



