import com.twitter.scalding._

class Count(args : Args) extends Job(args) {
    TextLine(args("input"))
        .flatMap('line -> 'filter) { line : String => line.split("\\s+") }
        .groupBy('filter) { _.size }
        .groupAll { _.sortBy('size) }
        .write( Tsv( args("output") ) )
}
