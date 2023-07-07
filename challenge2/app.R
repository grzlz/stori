library(shiny)
library(httr)
library(jpeg)

ui <- fluidPage(
  titlePanel("Image Resizer"),
  sidebarLayout(
    sidebarPanel(
      fileInput("file1", "Choose JPG Image",
                multiple = FALSE,
                accept = c("image/jpeg"))
    ),
    mainPanel(
      downloadButton("downloadButton", "Download")
    )
  )
)

server <- function(input, output) {
  output$originalImage <- renderPlot({
    inFile <- input$file1
    if (is.null(inFile))
      return(NULL)
    img <- readJPEG(inFile$datapath)
    plot(0:1,0:1,type="n",ann=FALSE,axes=FALSE)
    rasterImage(img,0,0,1,1)
  })
  
  output_file <- reactiveVal()  # output_file is a reactive value now
  
  observeEvent(input$file1, {   # create an observer to update output_file when a file is uploaded
    inFile <- input$file1
    if (is.null(inFile))
      return(NULL)
    
    img_data <- base64enc::base64encode(inFile$datapath)
    
    # Replace the URL with your API Gateway URL
    url <- "https://nsat8xqwdj.execute-api.us-west-1.amazonaws.com/prod/resizeImage/"
    response <- POST(url, body = img_data, encode = "raw", add_headers("Content-Type" = "text/plain"))
    
    if (status_code(response) == 200) {
      img_data <- content(response, "text")
      
      # decode the base64 string and write it to a binary file
      output_file <- tempfile(fileext = ".jpg")
      writeBin(base64enc::base64decode(img_data), output_file)
      
      output_file(output_file)  # update the reactive value
    }
  })
  
  # Setup download handler
  output$downloadButton <- downloadHandler(
    filename = function() { "thumbnail.jpg" },
    content = function(file) {
      file.copy(output_file(), file)  # copy the thumbnail to the download file path
    }
  )
}

# Run the application 
shinyApp(ui = ui, server = server)